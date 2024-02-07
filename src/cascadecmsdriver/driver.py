""" Driver module for interacting with Cascade CMS 8 REST API provided by Hannon Hill
for enterprise-scale content management. """

import requests
import logging
import json
from .cmstypes import *
from zeep import Client, xsd
from zeep.transports import Transport


class CascadeCMSRestDriver:
    def __init__(self, organization_name="", username="", password="", api_key="", verbose=False):
        self.setup_logging(verbose=verbose)
        self.info('Setting up new driver')
        self.organization_name = organization_name
        self.base_url = f'https://{self.organization_name}.cascadecms.com'
        self.session = requests.Session()
        if username == "" and password == "":
            assert api_key != ""
            self.debug(f"Using API Key: {api_key}")
            self.session.headers = {
                'Authorization': f'Bearer {api_key}'
            }
        if api_key == "":
            assert username != "" and password != ""
            print(f'Using username and password: {username, password}')
            self.session.auth = requests.auth.HTTPBasicAuth(username, password)

    def setup_logging(self, verbose=False):
        """ set up self.logger for Driver logging """
        self.logger = logging.getLogger('Cascade CMS Driver')
        formatter = logging.Formatter('%(prefix)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.prefix = {'prefix': 'Cascade REST Driver'}
        self.logger.addHandler(handler)
        self.logger = logging.LoggerAdapter(self.logger, self.prefix)
        if verbose:
            self.logger.setLevel(logging.DEBUG)
            self.logger.debug('Debug mode enabled', extra=self.prefix)
        else:
            self.logger.setLevel(logging.INFO)

    def debug(self, msg):
        self.logger.debug(msg, extra=self.prefix)

    def info(self, msg):
        self.logger.info(msg, extra=self.prefix)

    def error(self, msg):
        self.logger.error(msg, extra=self.prefix)

    def read_asset(self, asset_type='page', asset_identifier=None):
        """ read a CMS asset given its id and type"""
        url = f'{self.base_url}/api/v1/read/{asset_type}/{asset_identifier}'
        self.debug(f'Reading {asset_type} {asset_identifier} with {url}')
        return self.session.get(url).json()

    def read_asset_workflow_settings(self, asset_type='page', asset_identifier=None):
        """ read workflow settings on a specific asset """
        url = f'{self.base_url}/api/v1/readWorkflowSettings/{asset_type}/{asset_identifier}'
        self.debug(
            f'Reading {asset_type} {asset_identifier} workflow settings with {url}')
        return self.session.get(url).json()

    def edit_asset_workflow_settings(self, asset_type='page', asset_identifier=None, payload=None):
        """ edit workflow settings on a given asset of a given type.
        Include “workflowSettings” in message body based on {wsdl}.
        Its “identifier” property is not necessary since provided in URL.
        If “workflowSettings” is not provided, the folder will have all workflow
        definitions removed and workflow will not be required or inherited.
        This method requires the inclusion of workflow_settings. If you want to remove all workflow
        definitions, use the clear_asset_workflow_settings(asset_type,asset_identifier) method instead.
        """
        response = None
        if payload:
            # required keys in workflow settings
            if 'workflowSettings' in payload and \
                    all([x in payload['workflowSettings'] for x in ['workflowDefinitions', 'inheritWorkflows', 'requireWorkflow']]):
                url = f'{self.base_url}/api/v1/editWorkflowSettings/{asset_type}/{asset_identifier}'
                self.debug(
                    f'Editing workflow settings on {asset_type} {asset_identifier} with {url}')
                if isinstance(payload, dict):
                    self.debug(
                        'Payload is a dictionary; converting to JSON string with json.dumps()')
                    payload = json.dumps(payload)
                response = self.session.post(url, data=payload).json()

            else:
                self.error(
                    f'Not editing workflow settings on page {asset_identifier}; '
                    f'workflow settings must include keys workflowDefinitions '
                    '(asset identifiers list), inheritWorkflows (bool), requireWorkflow '
                    '(bool)'
                )
        else:
            self.error(
                f'Not editing workflow settings on page {asset_identifier}; '
                f'workflow settings not provided. Provide workflow settings based on WSDL'
            )
        return response

    def workflows_exist(self, workflow_settings):
        """ Determine whether any (1 or more) workflows are applied within a
        given readWorkflowSettings response"""
        workflow_settings = workflow_settings if 'workflowSettings' not in workflow_settings else workflow_settings[
            'workflowSettings']
        return len(workflow_settings['workflowDefinitions']) > 0 or \
            len(workflow_settings['workflowDefinitions']) > 0

    def get_user_by_email(self, email_address=""):
        return self.read_asset(asset_type='user', asset_identifier=email_address)

    def get_group(self, group_name):
        return self.read_asset(asset_type='group', asset_identifier=group_name)

    def publish_asset(self, asset_type='page', asset_identifier='', publish_information=None):
        url = f'{self.base_url}/api/v1/publish/{asset_type}/{asset_identifier}'
        self.debug(
            f'Publishing {asset_type} asset {asset_identifier} with {url}')
        if publish_information:
            self.debug(
                f'Publish information provided in request: {publish_information}')
            publish_information = json.dumps(publish_information)
        return self.session.post(url, data=publish_information).json()

    def unpublish_asset(self, asset_type='page', asset_identifier=''):
        self.debug(
            f'Unpublishing {asset_type} asset {asset_identifier}')
        return self.publish_asset(
            asset_type=asset_type,
            asset_identifier=asset_identifier,
            publish_information={
                'publishInformation': {
                    'unpublish': True
                }
            })

    def copy_asset_to_new_container(self, asset_type: str = 'page', asset_identifier: str = '', new_name: str = '', destination_container_identifier: str = ''):
        url = f'{self.base_url}/api/v1/copy/{asset_type}/{asset_identifier}'
        payload = json.dumps({
            'copyParameters': {
                'destinationContainerIdentifier': {
                    'type': 'folder',
                    'id': destination_container_identifier,
                },
                'doWorkflow': False,
                'newName': new_name,
            }
        })
        self.debug(f'Copying asset... POST payload {payload} to URL {url}')
        return self.session.post(url, data=payload).json()

    def batch(self, operations: [Operation]):
        # Returned entity name is "batchReturn"
        pass

    def checkIn(self, identifier: Identifier, comments: str):
        # Returned entity name is "checkInReturn"
        url = f'{self.base_url}/api/v1/checkIn/{identifier.type}/{identifier.id}'
        checkIn = CheckIn(identifier=identifier, comments=comments)
        return self.session.post(url, data=checkIn.toJson()).json()

    def checkOut(self, identifier: Identifier):
        # Returned entity name is "checkOutReturn"
        url = f'{self.base_url}/api/v1/checkOut/{identifier.type}/{identifier.id}'
        checkOut = CheckOut(identifier=identifier)
        return self.session.post(url, data=checkOut.toJson()).json()

    def copy(self, identifier: Identifier, copyParameters: CopyParameters, workflowConfiguration: WorkflowConfiguration):
        # Returned entity name is "copyReturn"
        url = f'{self.base_url}/api/v1/copy/{identifier.type}/{identifier.id}'
        copyPayload = Copy(
            identifier=identifier,
            copyParameters=copyParameters,
            workflowConfiguration=workflowConfiguration
        )
        return self.session.post(url, data=copyPayload.toJson()).json()

    def create(self, asset: Asset):
        # Returned entity name is "createReturn"
        pass

    def delete(self, identifier: Identifier, deleteParameters: DeleteParameters, workflowConfiguration: WorkflowConfiguration):
        # Returned entity name is "deleteReturn"
        pass

    def deleteMessage(self, identifier: Identifier):
        # Returned entity name is "deleteMessageReturn"
        pass

    def edit(self, asset: Asset):
        # Returned entity name is "editReturn"
        pass

    def editAccessRights(self, accessRightsInformation: AccessRightsInformation, applyToChildren: bool):
        # Returned entity name is "editAccessRightsReturn"
        pass

    def editPreference(self, preference: Preference):
        # Returned entity name is "editPreferenceReturn"
        pass

    def editWorkflowSettings(self, workflowSettings: WorkflowSettings, applyInheritWorkflowsToChildren: bool, applyRequireWorkflowToChildren: bool):
        # Returned entity name is "editWorkflowSettingsReturn"
        pass

    def listEditorConfigurations(self, identifier: Identifier):
        # Returned entity name is "listEditorConfigurationsReturn"
        pass

    def listMessages(self):
        # Returned entity name is "listMessagesReturn"
        pass

    def listSites(self):
        """ List all sites """
        url = f'{self.base_url}/api/v1/listSites'
        return self.session.get(url).json()

    def listSubscribers(self, identifier: Identifier):
        # Returned entity name is "listSubscribersReturn"
        pass

    def markMessage(self, identifier: Identifier, markType: MessageMarkType):
        # Returned entity name is "markMessageReturn"
        pass

    def move(self, identifier: Identifier, moveParameters: MoveParameters, workflowConfiguration: WorkflowConfiguration):
        # Returned entity name is "moveReturn"
        pass

    def performWorkflowTransition(self, workflowTransitionInformation: WorkflowTransitionInformation):
        # Returned entity name is "performWorkflowTransitionReturn"
        pass

    def publish(self, publishInformation: PublishInformation):
        # Returned entity name is "publishReturn"
        pass

    def read(self, identifier: Identifier):
        # Returned entity name is "readReturn"
        pass

    def readAccessRights(self, identifier: Identifier):
        url = f'{self.base_url}/api/v1/readAccessRights/{identifier.asset_type}/{identifier.asset_id}'
        return self.session.get(url).json()

    def readAudits(self, auditParameters: AuditParameters):
        # Returned entity name is "readAuditsReturn"
        pass

    def readPreferences(self):
        # Returned entity name is "readPreferencesReturn"
        pass

    def readWorkflowInformation(self, identifier: Identifier):
        # Returned entity name is "readWorkflowInformationReturn"
        pass

    def readWorkflowSettings(self, identifier: Identifier):
        # Returned entity name is "readWorkflowSettingsReturn"
        pass

    def search(self, searchInformation: SearchInformation):
        # Returned entity name is "searchReturn"
        pass

    def sendMessage(self, message: Message):
        # Returned entity name is "sendMessageReturn"
        pass

    def siteCopy(self, originalSiteId: str = '', originalSiteName: str = '', newSiteName: str = ''):
        url = f'{self.base_url}/api/v1/siteCopy'
        if originalSiteId.strip():
            key, val = 'originalSiteId', originalSiteId
        elif originalSiteName:
            key, val = 'originalSiteName', originalSiteName
        return self.session.post(url, data=json.dumps({
            key: val,
            'newSiteName': newSiteName
        })).json()
