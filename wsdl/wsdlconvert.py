from zeep import Client
from string import Template
import json
import zeep
from .types import *


class CascadeCMSRestDriver:
    def __init__(self, name="Cascade CMS Driver", organization_name="", username="", password="", api_key="", verbose=False):
        self.name = name
        self.verbose = verbose
        self.organization_name = organization_name
        self.base_url = f'https://{self.organization_name}.cascadecms.com'
        self.client = zeep.Client(
            f'{self.base_url}/ws/services/AssetOperationService?wsdl')
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
        self.session = requests.Session()
        self.session.headers = self.headers
        self.setup_logging(verbose=verbose)

    def setup_logging(self, verbose=False,):
        """ set up self.logger for Driver logging """
        self.logger = logging.getLogger(self.name)
        formatter = logging.Formatter('%(prefix)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.prefix = {'prefix': self.name}
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

    def batch(self, operations: [Operation]) -> [BatchResult]:
        # Returned entity name is "batchReturn"
        pass

    def checkIn(self, identifier: Identifier, comments: str) -> OperationResult:
        # Returned entity name is "checkInReturn"
        pass

    def checkOut(self, identifier: Identifier) -> CheckOutResult:
        # Returned entity name is "checkOutReturn"
        pass

    def copy(self, identifier: Identifier, copyParameters: CopyParameters, workflowConfiguration: WorkflowConfiguration) -> OperationResult:
        # Returned entity name is "copyReturn"
        pass

    def create(self, asset: Asset) -> CreateResult:
        # Returned entity name is "createReturn"
        pass

    def delete(self, identifier: Identifier, deleteParameters: DeleteParameters, workflowConfiguration: WorkflowConfiguration) -> OperationResult:
        # Returned entity name is "deleteReturn"
        pass

    def deleteMessage(self, identifier: Identifier) -> OperationResult:
        # Returned entity name is "deleteMessageReturn"
        pass

    def edit(self, asset: Asset) -> OperationResult:
        # Returned entity name is "editReturn"
        pass

    def editAccessRights(self, accessRightsInformation: AccessRightsInformation, applyToChildren: bool) -> OperationResult:
        # Returned entity name is "editAccessRightsReturn"
        pass

    def editPreference(self, preference: Preference) -> OperationResult:
        # Returned entity name is "editPreferenceReturn"
        pass

    def editWorkflowSettings(self, workflowSettings: WorkflowSettings, applyInheritWorkflowsToChildren: bool, applyRequireWorkflowToChildren: bool) -> OperationResult:
        # Returned entity name is "editWorkflowSettingsReturn"
        pass

    def listEditorConfigurations(self, identifier: Identifier) -> ListEditorConfigurationsResult:
        # Returned entity name is "listEditorConfigurationsReturn"
        pass

    def listMessages(self) -> ListMessagesResult:
        # Returned entity name is "listMessagesReturn"
        pass

    def listSites(self) -> ListSitesResult:
        # Returned entity name is "listSitesReturn"
        pass

    def listSubscribers(self, identifier: Identifier) -> ListSubscribersResult:
        # Returned entity name is "listSubscribersReturn"
        pass

    def markMessage(self, identifier: Identifier, markType: MessageMarkType) -> OperationResult:
        # Returned entity name is "markMessageReturn"
        pass

    def move(self, identifier: Identifier, moveParameters: MoveParameters, workflowConfiguration: WorkflowConfiguration) -> OperationResult:
        # Returned entity name is "moveReturn"
        pass

    def performWorkflowTransition(self, workflowTransitionInformation: WorkflowTransitionInformation) -> OperationResult:
        # Returned entity name is "performWorkflowTransitionReturn"
        pass

    def publish(self, publishInformation: PublishInformation) -> OperationResult:
        # Returned entity name is "publishReturn"
        pass

    def read(self, identifier: Identifier) -> ReadResult:
        # Returned entity name is "readReturn"
        pass

    def readAccessRights(self, identifier: Identifier) -> ReadAccessRightsResult:
        # Returned entity name is "readAccessRightsReturn"
        pass

    def readAudits(self, auditParameters: AuditParameters) -> ReadAuditsResult:
        # Returned entity name is "readAuditsReturn"
        pass

    def readPreferences(self) -> ReadPreferencesResult:
        # Returned entity name is "readPreferencesReturn"
        pass

    def readWorkflowInformation(self, identifier: Identifier) -> ReadWorkflowInformationResult:
        # Returned entity name is "readWorkflowInformationReturn"
        pass

    def readWorkflowSettings(self, identifier: Identifier) -> ReadWorkflowSettingsResult:
        # Returned entity name is "readWorkflowSettingsReturn"
        pass

    def search(self, searchInformation: SearchInformation) -> SearchResult:
        # Returned entity name is "searchReturn"
        pass

    def sendMessage(self, message: Message) -> OperationResult:
        # Returned entity name is "sendMessageReturn"
        pass

    def siteCopy(self, originalSiteId: str, originalSiteName: str, newSiteName: str) -> OperationResult:
        # Returned entity name is "siteCopyReturn"
        pass
