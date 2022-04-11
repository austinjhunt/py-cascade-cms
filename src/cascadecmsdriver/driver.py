""" Driver module for interacting with Cascade CMS 8 REST API provided by Hannon Hill 
for enterprise-scale content management. """

import requests
import logging
import json


class CascadeCMSRestDriver:
    def __init__(self, organization_name="", username="", password="", api_key="", verbose=False):
        self.verbose = verbose
        self.organization_name = organization_name
        self.base_url = f'https://{self.organization_name}.cascadecms.com'
        if username == "" and password == "":
            assert api_key != ""
            self.headers = {
                'Authorization': f'Bearer {api_key}'
            }
        if api_key == "":
            assert username != "" and password != ""
            authstring = f'{username}:{password}'.encode('ascii')
            self.headers = {
                'Authorization': f'Bearer {authstring}'
            }
        self.setup_logging(verbose=verbose)

    def setup_logging(self, verbose=False):
        """ set up self.logger for Driver logging """
        self.logger = logging.getLogger('DataManager')
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

    def list_sites(self):
        """ List all sites """
        url = f'{self.base_url}/api/v1/listSites'
        self.debug(f"Listing all sites with {url}")
        return requests.get(url, headers=self.headers).json()

    def read_asset(self, asset_type='page', asset_identifier=None):
        """ read a CMS asset given its id and type"""
        url = f'{self.base_url}/api/v1/read/{asset_type}/{asset_identifier}'
        self.debug(f'Reading {asset_type} {asset_identifier} with {url}')
        return requests.get(url, headers=self.headers).json()

    def read_asset_workflow_settings(self, asset_type='page', asset_identifier=None):
        """ read workflow settings on a specific asset """
        url = f'{self.base_url}/api/v1/readWorkflowSettings/{asset_type}/{asset_identifier}'
        self.debug(
            f'Reading {asset_type} {asset_identifier} workflow settings with {url}')
        return requests.get(url, headers=self.headers).json()

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
                response = requests.post(
                    url=url, headers=self.headers, data=payload).json()

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
