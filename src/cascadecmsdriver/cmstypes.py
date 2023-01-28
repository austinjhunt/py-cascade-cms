from datetime import datetime, time
from typing import Union
from enum import Enum
import json


class Entity:
    pass


class Id:
    pass


class Idref:
    pass


class Idrefs:
    pass


class Ncname:
    pass


class Nmtoken:
    pass


class Nmtokens:
    pass


class Notation:
    pass


class Name:
    pass


class Qname:
    pass


class Anysimpletype:
    pass


class Anyuri:
    pass


class Base64binary:
    pass


class Boolean:
    pass


class Byte:
    pass


class Date:
    pass


class Datetime:
    pass


class Decimal:
    pass


class Double:
    pass


class Duration:
    pass


class Float:
    pass


class Gday:
    pass


class Gmonth:
    pass


class Gmonthday:
    pass


class Gyear:
    pass


class Gyearmonth:
    pass


class Hexbinary:
    pass


class Int:
    pass


class Integer:
    pass


class Language:
    pass


class Long:
    pass


class Negativeinteger:
    pass


class Nonnegativeinteger:
    pass


class Nonpositiveinteger:
    pass


class Normalizedstring:
    pass


class Positiveinteger:
    pass


class Short:
    pass


class String:
    pass


class Time:
    pass


class Token:
    pass


class Unsignedbyte:
    pass


class Unsignedint:
    pass


class Unsignedlong:
    pass


class Unsignedshort:
    pass


class JSONSerializable:
    def toJson(self):
        return json.dumps(self.__dict__)


class EntityType(str, Enum):
    assetFactory = "assetfactory"
    assetFactoryContainer = "assetfactorycontainer"
    block = "block"
    blockFeed = "block_FEED"
    blockIndex = "block_INDEX"
    blockText = "block_TEXT"
    blockXHTMLDataDefinition = "block_XHTML_DATADEFINITION"
    blockXML = "block_XML"
    blockTwitterFeed = "block_TWITTER_FEED"
    connectorContainer = "connectorcontainer"
    # twitterconnector cannot be removed from here otherwise reading audits via WS can break  -->
    twitterConnector = "twitterconnector"
    facebookConnector = "facebookconnector"
    wordpressConnector = "wordpressconnector"
    googleAnalyticsConnector = "googleanalyticsconnector"
    contentType = "contenttype"
    contentTypeContainer = "contenttypecontainer"
    destination = "destination"
    editorConfiguration = "editorconfiguration"
    _file = "file"
    folder = "folder"
    group = "group"
    message = "message"
    metadataSet = "metadataset"
    metadataSetContainer = "metadatasetcontainer"
    page = "page"
    pageConfigurationSet = "pageconfigurationset"
    pageConfiguration = "pageconfiguration"
    pageRegion = "pageregion"
    pageConfigurationSetContainer = "pageconfigurationsetcontainer"
    publishSet = "publishset"
    publishSetContainer = "publishsetcontainer"
    reference = "reference"
    role = "role"
    dataDefinition = "datadefinition"
    dataDefinitioncontainer = "datadefinitioncontainer"
    sharedField = "sharedfield"
    sharedFieldcontainer = "sharedfieldcontainer"
    _format = "format"
    formatXSLT = "format_XSLT"
    formatScript = "format_SCRIPT"
    site = "site"
    siteDestinationContainer = "sitedestinationcontainer"
    symlink = "symlink"
    target = "target"
    template = "template"
    transport = "transport"
    transportFS = "transport_fs"
    transportFTP = "transport_ftp"
    transportDB = "transport_db"
    transportCloud = "transport_cloud"
    transportContainer = "transportcontainer"
    user = "user"
    workflow = "workflow"
    workflowDefinition = "workflowdefinition"
    workflowDefinitionContainer = "workflowdefinitioncontainer"
    workflowEmail = "workflowemail"
    workflowEmailContainer = "workflowemailcontainer"


class NamingRuleAsset:
    pass


class NamingRuleCase:
    pass


class NamingRuleSpacing:
    pass


class SerializationType:
    pass


class StructuredDataAssetType:
    pass


class DynamicMetadataFieldType:
    pass


class MetadataFieldVisibility:
    pass


class RecycleBinExpiration:
    pass


class AuditTypes(Enum):
    login = "login"
    loginFailed = "login_failed"
    logout = "logout"
    startWorkflow = "start_workflow"
    advanceWorkflow = "advance_workflow"
    edit = "edit"
    copy = "copy"
    create = "create"
    reference = "reference"
    delete = "delete"
    deleteUnpublish = "delete_unpublish"
    checkIn = "check_in"
    checkOut = "check_out"
    activateVersion = "activate_version"
    publish = "publish"
    unpublish = "unpublish"
    recycle = "recycle"
    restore = "restore"
    move = "move"


class AllLevel:
    pass


class AclEntryType:
    pass


class AclEntryLevel:
    pass


class AuthMode:
    pass


class AssetFactoryWorkflowMode:
    pass


class ContentTypePageConfigurationPublishMode:
    pass


class FtpProtocolType:
    pass


class IndexBlockPageXml:
    pass


class IndexBlockRenderingBehavior:
    pass


class IndexBlockSortMethod:
    pass


class IndexBlockSortOrder:
    pass


class IndexBlockType:
    pass


class InlineEditableFieldType:
    pass


class LinkRewriting:
    pass


class Message:
    def __init__(self, _id: str, To: str, From: str, Subject: str, Date: datetime, Body: str):
        pass


class MessageMarkType:
    pass


class RoleTypes:
    pass


class ScheduledDestinationMode:
    pass


class SiteLinkRewriting:
    pass


class StructuredDataType:
    pass


class TwitterQueryType:
    pass


class UserAuthTypes:
    pass


class DayOfWeek(Enum):
    monday = "Monday"
    tuesday = "Tuesday"
    wednesday = "Wednesday"
    thursday = "Thursday"
    friday = "Friday"
    saturday = "Saturday"
    sunday = "Sunday"


class SiteAbilities:
    # WSDL HAS TYPO: bypassWorkflowDefintionGroupsForFolders should be bypassWorkflowDefinitionGroupsForFolders
    def __init__(self, bypassAllPermissionsChecks: bool, uploadImagesFromWYSIWYG: bool, multiselectCopy: bool, multiselectPublish: bool, multiselectmove: bool, multiselectDelete: bool, editPageLevelConfigurations: bool, editPageContentType: bool, editDataDefinition: bool, publishReadableHomeAssets: bool, publishWritableHomeAssets: bool, editAccessRights: bool, viewVersions: bool, activateDeleteVersions: bool, accessAudits: bool, bypassWorkflow: bool, assignApproveWorkflowSteps: bool, deleteWorkflows: bool, breakLocks: bool, assignWorkflowsToFolders: bool, bypassAssetFactoryGroupsNewMenu: bool, bypassDestinationGroupsWhenPublishing: bool, Bypassworkflowdefintiongroupsforfolders: bool, accessManageSiteArea: bool, accessAssetFactories: bool, accessConfigurationSets: bool, accessDataDefinitions: bool, Accesssharedfields: bool, Accessmetadatasets: bool, Accesspublishsets: bool, Accessdestinations: bool, Accesstransports: bool, Accessworkflowdefinitions: bool, Accessworkflowemails: bool, Accesscontenttypes: bool, Accessconnectors: bool, Publishreadableadminareaassets: bool, Publishwritableadminareaassets: bool, Importziparchive: bool, Bulkchange: bool, Recyclebinviewrestoreuserassets: bool, Recyclebindeleteassets: bool, Recyclebinviewrestoreallassets: bool, Moverenameassets: bool, Diagnostictests: bool, Alwaysallowedtotoggledatachecks: bool, Viewpublishqueue: bool, Reorderpublishqueue: bool, Cancelpublishjobs: bool, Sendstaleassetnotifications: bool, Brokenlinkreportaccess: bool, Brokenlinkreportmarkfixed: bool, Accesseditorconfigurations: bool, Bypasswysiwygeditorrestrictions: bool, Accesssiteimproveintegration: bool):
        pass


class Preference:
    def __init__(self, name: str, Value: str):
        pass


class Path:
    def __init__(self, path: str, siteId: str, siteName: str):
        self.path = path
        self.siteId = siteId
        self.siteName = siteName


class Identifier(JSONSerializable):
    def __init__(self, assetId: str, asset_type: EntityType, path: Path = None, recycled: bool = None):
        self.id = assetId
        self.type = asset_type
        self.path = path
        self.recycled = recycled


class InlineEditableField:
    def __init__(self, pageConfigurationName: str, Pageregionname: str, Datadefinitiongrouppath: str, _type: InlineEditableFieldType, name: str):
        pass


class ContainerChildren:
    def __init__(self, containerChildren: list[Identifier]):
        pass


class NamedAsset:
    def __init__(self, _id: str, name: str):
        pass


class FieldValue:
    def __init__(self, value: str):
        pass


class WorkflowStepConfiguration:
    def __init__(self, Stepidentifier: str, Stepassignment: str):
        pass


class WorkflowConfiguration:
    def __init__(self, workflowName: str, workflowDefinitionId: str, workflowDefinitionPath: str, workflowComments: str, workflowStepConfigurations: list[WorkflowStepConfiguration], endDate: datetime):
        self.workflowName = workflowName
        self.workflowDefinitionId = workflowDefinitionId
        self.workflowDefinitionPath = workflowDefinitionPath
        self.workflowComments = workflowComments
        self.workflowStepConfigurations = workflowStepConfigurations
        self.endDate = endDate


class AclEntry:
    def __init__(self, Level: AclEntryLevel, _type: AclEntryType, name: str):
        pass


class AccessRightsInformation:
    def __init__(self, identifier: Identifier, aclEntries: list[AclEntry], allLevel: AllLevel):
        pass


class Asset:
    def __init__(self, workflowConfiguration: WorkflowConfiguration):
        pass


class AssetFactoryPluginParameter:
    def __init__(self, name: str, Value: str):
        pass


class AssetFactoryPlugin:
    def __init__(self, name: str, parameters: list[AssetFactoryPluginParameter]):
        pass


class AssetFactory:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, applicableGroups: str, assetType: str, baseAssetId: str, baseAssetPath: str, baseAssetPRecycled: bool, description: str, placementFolderId: str, placementFolderPath: str, placementFolderRecycled: bool, allowSubfolderPlacement: bool, folderPlacementPosition: int, overwrite: bool, workflowMode: AssetFactoryWorkflowMode, workflowDefinitionId: str, workflowDefinitionPath: str, plugins: list[AssetFactoryPlugin]):
        pass


class AssetFactoryContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, applicableGroups: str, description: str, children: ContainerChildren):
        pass


class Audit:
    def __init__(self, user: str, action: AuditTypes, identifier: Identifier, date: datetime):
        pass


class Tag:
    def __init__(self, name: str):
        pass


class DynamicMetadataFieldDefinitionValue:
    def __init__(self, value: str, label: str, selectedByDefault: bool):
        pass


class DynamicMetadataFieldDefinition:
    def __init__(self, name: str, Label: str, fieldType: DynamicMetadataFieldType, Required: bool, Visibility: MetadataFieldVisibility, Possiblevalues: list[DynamicMetadataFieldDefinitionValue], helpText: str):
        pass


class DynamicMetadataField:
    def __init__(self, name: str, fieldValues: list[FieldValue]):
        pass


class Metadata:
    def __init__(self, author: str, displayName: str, endDate: datetime, keywords: str, metadescription: str, reviewDate: datetime, startDate: datetime, summary: str, teaser: str, title: str, dynamicFields: list[DynamicMetadataField]):
        pass


class WorkflowNamingBehavior:
    pass


class WorkflowAction:
    def __init__(self, identifier: str, Label: str, Actiontype: str, NextId: str):
        pass


class WorkflowStep:
    def __init__(self, identifier: str, Label: str, Steptype: str, Owner: str, Actions: list[WorkflowAction]):
        pass


class Workflow:
    def __init__(self, _id: str, name: str, Relatedentity: Identifier, Currentstep: str, Orderedsteps: list[WorkflowStep], Unorderedsteps: list[WorkflowStep], startDate: datetime, endDate: datetime, completedWorkflowEmailId: str, completedWorkflowEmailPath: str, notificationWorkflowEmailId: str, notificationWorkflowEmailPath: str):
        pass


class WorkflowDefinition:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, applicableGroups: str, copy: bool, create: bool, delete: bool, edit: bool, move: bool, namingBehavior: WorkflowNamingBehavior, xml: str, completedWorkflowEmailId: str, completedWorkflowEmailPath: str, notificationWorkflowEmailId: str, notificationWorkflowEmailPath: str):
        pass


class WorkflowDefinitionContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class WorkflowEmail:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, Subject: str, Body: str):
        pass


class WorkflowEmailContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class WorkflowSettings:
    def __init__(self, identifier: Identifier, workflowDefinitions: list[Identifier], inheritWorkflows: bool, requireWorkflow: bool, inheritedWorkflowDefinitions: list[Identifier]):
        pass


class EditWorkflowSettings:
    def __init__(self, workflowSettings: WorkflowSettings, applyInheritWorkflowsToChildren: bool, applyRequireWorkflowToChildren: bool):
        pass


class ListSubscribers:
    def __init__(self, identifier: Identifier):
        pass


class PublishIntervalHours:
    def __init__(self, hours: int):
        pass


class PublishDaysOfWeek:
    def __init__(self, daysOfWeek: list[DayOfWeek]):
        pass


class CronExpression:
    def __init__(self, cronExpression: str):
        pass


class PublishInformation:
    def __init__(self, identifier: Identifier, destinations: list[Identifier], unpublish: bool, publishRelatedAssets: bool, publishRelatedpublishSet: bool, scheduledDate: datetime):
        pass


class Publish:
    def __init__(self, Publishinformation: PublishInformation):
        pass


class PublishSet:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, files: list[Identifier], folders: list[Identifier], pages: list[Identifier], useScheduledPublishing: bool, scheduledPublishDestinationMode: ScheduledDestinationMode, scheduledPublishDestinations: list[Identifier], timeToPublish: time, choice: Union[PublishIntervalHours, PublishDaysOfWeek, CronExpression], sendReportToUsers: str, sendReportToGroups: str, sendReportOnErrorOnly: bool):
        pass


class PublishSetContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class PublishableAsset:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, shouldBePublished: bool, shouldBeIndexed: bool, lastPublishedDate: datetime, lastPublishedBy: str):
        pass


class StructuredDataNode:
    def __init__(self, _type: StructuredDataType, identifier: str, structuredDataNodes: list, text: str, assetType: StructuredDataAssetType, blockId: str, blockPath: str, fileId: str, filePath: str, pageId: str, pagePath: str, symLinkId: str, symLinkPath: str, recycled: bool):
        pass


class StructuredData:
    def __init__(self, definitionId: str, definitionPath: str, structuredDataNodes: list[StructuredDataNode]):
        pass


class MetadataSet:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, authorFieldRequired: bool, authorFieldVisibility: MetadataFieldVisibility, authorFieldHelpText: str, descriptionFieldRequired: bool, descriptionFieldVisibility: MetadataFieldVisibility, descriptionFieldHelpText: str, displayNameFieldRequired: bool, displayNameFieldVisibility: MetadataFieldVisibility, displayNameFieldHelpText: str, endDateFieldRequired: bool, endDateFieldVisibility: MetadataFieldVisibility, endDateFieldHelpText: str, expirationFolderFieldRequired: bool, expirationFolderFieldVisibility: MetadataFieldVisibility, expirationFolderFieldHelpText: str, keywordsFieldRequired: bool, keywordsFieldVisibility: MetadataFieldVisibility, keywordsFieldHelpText: str, reviewDateFieldRequired: bool, reviewDateFieldVisibility: MetadataFieldVisibility, reviewDateFieldHelpText: str, startDateFieldRequired: bool, startDateFieldVisibility: MetadataFieldVisibility, startDateFieldHelpText: str, summaryFieldRequired: bool, summaryFieldVisibility: MetadataFieldVisibility, summaryFieldHelpText: str, teaserFieldRequired: bool, teaserFieldVisibility: MetadataFieldVisibility, teaserFieldHelpText: str, titleFieldRequired: bool, titleFieldVisibility: MetadataFieldVisibility, titleFieldHelpText: str, dynamicMetadataFieldDefinitions: list[DynamicMetadataFieldDefinition]):
        pass


class MetadataSetContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class WorkflowTransitionInformation:
    def __init__(self, WorkflowId: str, Actionidentifier: str, Transitioncomment: str):
        pass


class XhtmlDataDefinitionBlock:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, structureddata: StructuredData, Xhtml: str):
        pass


class XmlBlock:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, xml: str):
        pass


class XsltFormat:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], xml: str):
        pass


class Symlink:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, linkUrl: str):
        pass


class AuditParameters:
    def __init__(self, identifier: Identifier, username: str, groupname: str, roleName: str, startDate: datetime, endDate: datetime, auditType: AuditTypes):
        pass


class Authentication:
    def __init__(self, password: str = "", username: str = "", apiKey: str = ""):
        """ Unless an apiKey is provided, username and password are required """
        self.password = password
        self.username = username
        self.apiKey = apiKey


class BaseAsset:
    def __init__(self, _id: str):
        pass


class Block:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool):
        pass


### BEGIN OPERATIONS ###

class Audit:
    def __init__(self, user: str, action: AuditTypes, identifier: Identifier, date: datetime):
        pass


class CheckIn(JSONSerializable):
    def __init__(self, identifier: Identifier, comments: str):
        self.checkInRequest = {
            'identifier': identifier.toJson(),
            'comments': comments
        }


class CheckOut(JSONSerializable):
    def __init__(self, identifier: Identifier):
        self.checkOutRequest = {
            'identifier': identifier.toJson()
        }


class CopyParameters():
    def __init__(self, destinationContainerIdentifier: Identifier, doWorkflow: bool, newName: str):
        self.destinationContainerIdentifier = destinationContainerIdentifier
        self.doWorkflow = doWorkflow
        self.newName = newName


class Copy(JSONSerializable):
    def __init__(self, identifier: Identifier, copyParameters: CopyParameters, workflowConfiguration: WorkflowConfiguration):

        self.copyRequest = {
            'identifier': identifier.toJson(),
            'copyParameters': copyParameters.toJson(),
            'workflowConfiguration': workflowConfiguration.toJson()
        }


class Create:
    def __init__(self, asset: Asset):
        pass


class DeleteParameters:
    def __init__(self, unpublish: bool, destinations: list[Identifier], doWorkflow: bool):
        pass


class Delete:
    def __init__(self, workflowConfiguration: WorkflowConfiguration, identifier: Identifier, deleteParameters: DeleteParameters):
        pass


class Edit:
    def __init__(self, asset: Asset):
        pass


class EditAccessRights:
    def __init__(self, accessRightsInformation: AccessRightsInformation, applyToChildren: bool):
        pass


class MoveParameters:
    def __init__(self, unpublish: bool, destinations: list[Identifier], destinationContainerIdentifier: Identifier, doWorkflow: bool, newName: str):
        pass


class Move:
    def __init__(self, identifier: Identifier, moveParameters: MoveParameters, workflowConfiguration: WorkflowConfiguration):
        pass


class Read:
    def __init__(self, identifier: Identifier):
        pass


class ReadAccessRights:
    def __init__(self, identifier: Identifier):
        pass


class ReadWorkflowSettings:
    def __init__(self, identifier: Identifier):
        pass


class ReadWorkflowSettingsResult:
    def __init__(self, success: str, message: str, workflowSettings: WorkflowSettings):
        pass


class SiteCopy:
    def __init__(self, originalSiteId: str, originalSiteName: str, newSiteName: str):
        pass

### END OPERATIONS ###

### RESULTS ###


class CheckOutResult:
    def __init__(self, success: str, message: str, Workingcopyidentifier: Identifier):
        pass


class CreateResult:
    def __init__(self, success: str, message: str, createdAssetId: str):
        pass


class EditPreferenceResult:
    def __init__(self, preference: Preference):
        pass


class ListEditorConfigurationsResult:
    def __init__(self, success: str, message: str, editorConfigurations: list[Identifier]):
        pass


class ListMessagesResult:
    def __init__(self, success: str, message: str, Messages: list[Message]):
        pass


class ListSitesResult:
    def __init__(self, success: str, message: str, sites: list[Identifier]):
        pass


class ListSubscribersResult:
    def __init__(self, success: str, message: str, subscribers: list[Identifier], manualSubscribers: list[Identifier]):
        pass


class OperationResult:
    def __init__(self, success: str, message: str):
        pass


class SearchMatches:
    def __init__(self, searchMatches: list[Identifier]):
        pass


class SearchResult:
    def __init__(self, success: str, message: str, Matches: SearchMatches):
        pass


class ReadAccessRightsResult:
    def __init__(self, success: str, message: str, accessRightsInformation: AccessRightsInformation):
        pass


class ReadAuditsResult:
    def __init__(self, success: str, message: str, Audits: list[Audit]):
        pass


class ReadPreferencesResult:
    def __init__(self, success: str, message: str, preferences: list[Preference]):
        pass


class ReadResult:
    def __init__(self, success: str, message: str, asset: Asset):
        pass


class ReadWorkflowInformationResult:
    def __init__(self, success: str, message: str, workflow: Workflow):
        pass


class BatchResult:
    def __init__(self, batchResult: Union[OperationResult, CheckOutResult,
                                          CreateResult, ListMessagesResult, ReadResult,
                                          ReadAccessRightsResult, ReadWorkflowSettingsResult,
                                          ReadAuditsResult, ListSubscribersResult, SearchResult,
                                          ReadWorkflowInformationResult]):
        pass


### END RESULTS ###

class Operation:
    def __init__(self, operation: Union[Create, Delete, Edit, Publish, Read, ReadAccessRights, EditAccessRights, ReadWorkflowSettings, EditWorkflowSettings, ListSubscribers, CheckOut, CheckIn, Copy, SiteCopy]):
        self.operation = operation


class CloudTransport:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, Key: str, Secret: str, Bucketname: str, Basepath: str):
        pass


class ConnectorParameter:
    def __init__(self, name: str, value: str):
        pass


class ConnectorContentTypeLinkParam:
    def __init__(self, name: str,  value: str):
        pass


class ConnectorContentTypeLink:
    def __init__(self, contentTypeId: str, contentTypePath: str, pageConfigurationId: str, pageConfigurationName: str, connectorContentTypeLinkParams: list[ConnectorContentTypeLinkParam]):
        pass


class Connector:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, auth1: str, auth2: str, url: str, verified: bool, verifiedDate: datetime, connectorParameters: list[ConnectorParameter], Connectorcontenttypelinks: list[ConnectorContentTypeLink]):
        pass


class ConnectorContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class ContaineredAsset:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str):
        pass


class ContentTypePageConfiguration:
    def __init__(self, pageConfigurationId: str, pageConfigurationName: str, Publishmode: ContentTypePageConfigurationPublishMode, destinations: list[Identifier]):
        pass


class ContentType:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, pageConfigurationSetId: str, pageConfigurationSetPath: str, metadatasetId: str, metadatasetPath: str, dataDefinitionId: str, dataDefinitionPath: str, editorConfigurationId: str, editorConfigurationPath: str, publishSetId: str, publishSetPath: str, contentTypePageConfigurations: list[ContentTypePageConfiguration], inlineEditableFields: list[InlineEditableField]):
        pass


class ContentTypeContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class Datadefinition:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, xml: str):
        pass


class Datadefinitioncontainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class Databasetransport:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, Transportsiteid: int, Servername: str, Serverport: int, Databasename: str, Username: str, Password: str):
        pass


class Destination:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, TransportId: str, Transportpath: str, applicableGroups: str, Directory: str, Enabled: bool, Checkedbydefault: bool, Publishascii: bool, useScheduledPublishing: bool, scheduledPublishDestinationMode: ScheduledDestinationMode, scheduledPublishDestinations: list[Identifier], timeToPublish: time, choice: Union[PublishIntervalHours, PublishDaysOfWeek, CronExpression], sendReportToUsers: str, sendReportToGroups: str, sendReportOnErrorOnly: bool, Weburl: str, extensionsToStrip: str, siteId: str, siteName: str):
        pass


class DublinAwareAsset:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int):
        pass


class EditorConfiguration:
    def __init__(self, _id: str, name: str, siteId: str, siteName: str, cssFileId: str, cssFilePath: str, cssFileRecycled: bool, configuration: str):
        pass


class ExpiringAsset:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool):
        pass


class FacebookConnector:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, auth1: str, auth2: str, url: str, verified: bool, verifiedDate: datetime, connectorParameters: list[ConnectorParameter], Connectorcontenttypelinks: list[ConnectorContentTypeLink], DestinationId: str, Destinationpath: str):
        pass


class Feedblock:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, feedUrl: str):
        pass


class File:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, shouldBePublished: bool, shouldBeIndexed: bool, lastPublishedDate: datetime, lastPublishedBy: str, text: str, data: bytes, rewriteLinks: bool, linkRewriting: LinkRewriting):
        pass


class Filesystemtransport:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, Directory: str):
        pass


class Folder:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, shouldBePublished: bool, shouldBeIndexed: bool, lastPublishedDate: datetime, lastPublishedBy: str, children: ContainerChildren, includeInStaleContent: bool):
        pass


class FolderContainedAsset:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag]):
        pass


class Ftptransport:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, Hostname: str, Port: int, Dopasv: bool, Username: str, Authmode: AuthMode, Privatekey: str, Password: str, Directory: str, Ftpprotocoltype: FtpProtocolType):
        pass


class GlobalAbilities:
    def __init__(self, bypassAllPermissionsChecks: bool, accessSiteManagement: bool, createSites: bool, editAccessRights: bool, accessAudits: bool, accessAllSites: bool, viewSystemInfoAndLogs: bool, forceLogout: bool, diagnosticTests: bool, accessSecurityArea: bool, optimizeDatabase: bool, syncLdap: bool, configureLogging: bool, searchingIndexing: bool, accessConfiguration: bool, editSystemPreferences: bool, broadcastMessages: bool, viewUsersInMemberGroups: bool, viewAllUsers: bool, createUsers: bool, deleteUsersInMemberGroups: bool, deleteAllUsers: bool, viewMemberGroups: bool, viewAllGroups: bool, createGroups: bool, deleteMemberGroups: bool, accessRoles: bool, createRoles: bool, deleteAnyGroup: bool, editAnyUser: bool, editUsersInMemberGroups: bool, editAnyGroup: bool, editMemberGroups: bool, databaseExporttool: bool, changeIdentity: bool, accessDefaultEditorConfiguration: bool, modifyDictionary: bool):
        pass


class GoogleAnalyticsConnector:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, auth1: str, auth2: str, url: str, verified: bool, verifiedDate: datetime, connectorParameters: list[ConnectorParameter], ConnectorContentTypelinks: list[ConnectorContentTypeLink]):
        pass


class Group:
    def __init__(self, Groupname: str, Users: str, Role: str):
        pass


class IndexBlock:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, indexBlockType: IndexBlockType, indexedFolderId: str, indexedFolderPath: str, indexedcontentTypeId: str, indexedcontentTypePath: str, indexedFolderRecycled: bool, maxRenderedAssets: int, depthOfIndex: int, renderingBehavior: IndexBlockRenderingBehavior, indexPages: bool, indexBlocks: bool, Indexlinks: bool, indexFiles: bool, indexRegularContent: bool, indexSystemMetadata: bool, indexUserMetadata: bool, indexAccessRights: bool, indexTags: bool, indexUserInfo: bool, indexWorkflowInfo: bool, appendCallingPageData: bool, sortMethod: IndexBlockSortMethod, sortOrder: IndexBlockSortOrder, pageXml: IndexBlockPageXml):
        pass


class PageRegion:
    def __init__(self, _id: str, name: str, BlockId: str, Blockpath: str, Blockrecycled: bool, Noblock: bool, formatId: str, FormatPath: str, formatRecycled: bool, Noformat: bool):
        pass


class PageConfiguration:
    def __init__(self, _id: str, name: str, defaultConfiguration: bool, templateId: str, templatePath: str, formatId: str, FormatPath: str, formatRecycled: bool, pageRegions: list[PageRegion], outputExtension: str, serializationType: SerializationType, includeXmlDeclaration: bool, publishable: bool):
        pass


class PageConfigurationSet:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, pageConfigurations: list[PageConfiguration]):
        pass


class PageConfigurationSetContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class Page:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, shouldBePublished: bool, shouldBeIndexed: bool, lastPublishedDate: datetime, lastPublishedBy: str, configurationSetId: str, configurationSetPath: str, contentTypeId: str, contentTypePath: str, structuredData: StructuredData, Xhtml: str, pageConfigurations: list[PageConfiguration], Linkrewriting: LinkRewriting):
        pass


class Reference:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], ReferencedassetId: str, Referencedassetpath: str, Referencedassettype: EntityType):
        pass


class Role:
    def __init__(self, _id: str, name: str, Roletype: RoleTypes, choice: Union[GlobalAbilities, SiteAbilities]):
        pass


class RoleAssignment:
    def __init__(self, RoleId: str, Rolename: str, Users: str, Groups: str):
        pass


class Scriptformat:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], Script: str):
        pass


class SearchFieldString:
    pass


class SearchFields:
    def __init__(self, searchField: list[SearchFieldString]):
        pass


class SearchTypes:
    def __init__(self, searchtypes: list[EntityType]):
        pass


class SearchInformation:
    def __init__(self, Searchterms: str, siteId: str, siteName: str, searchFields: SearchFields, Searchtypes: SearchTypes):
        pass


class SharedField:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, xml: str):
        pass


class SharedFieldContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class PublishDaysOfWeek:
    def __init__(self, daysOfWeek: list[DayOfWeek]):
        pass


class Site:
    def __init__(self, _id: str, name: str, url: str, extensionsToStrip: str, defaultMetadataSetId: str, defaultMetadataSetPath: str, siteAssetFactoryContainerId: str, siteAssetFactoryContainerPath: str, defaultEditorConfigurationId: str, defaultEditorConfigurationPath: str, siteStartingPageId: str, siteStartingPagePath: str, siteStartingPageRecycled: bool, roleAssignments: list[RoleAssignment], useScheduledPublishing: bool, scheduledPublishDestinationMode: ScheduledDestinationMode, scheduledPublishDestinations: list[Identifier], timeToPublish: time,  choice: Union[PublishIntervalHours, PublishDaysOfWeek, CronExpression], sendReportToUsers: str, sendReportToGroups: str, sendReportOnErrorOnly: bool, recycleBinExpiration: RecycleBinExpiration, unpublishExpiration: bool, linkCheckerEnabled: bool, externalLinkCheckOnPublish: bool, inheritDataChecksEnabled: bool, spellcheckEnabled: bool, linkCheckEnabled: bool, accessibilityCheckEnabled: bool, inheritNamingRules: bool, namingRuleCase: NamingRuleCase, namingRuleSpacing: NamingRuleSpacing, namingRuleAssets: list[NamingRuleAsset], AccessibilityCheckerEnabled: bool, siteImproveIntegrationEnabled: bool, siteImproveUrl: str, widenDamIntegrationEnabled: bool, widenDamIntegrationCategory: str, webdamDamIntegrationEnabled: bool, rootFolderId: str, rootAssetFactoryContainerId: str, rootPageConfigurationSetContainerId: str, rootContentTypeContainerId: str, rootConnectorContainerId: str, rootDataDefinitionContainerId: str, rootSharedFieldContainerId: str, rootMetaDatasetContainerId: str, rootPublishSetContainerId: str, rootSiteDestinationContainerId: str, rootTransportContainerId: str, rootWorkflowDefinitionContainerId: str, rootWorkflowEmailContainerId: str, linkRewriting: SiteLinkRewriting):
        pass


class SiteDestinationContainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class StatusUpdateConnector:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, auth1: str, auth2: str, url: str, verified: bool, verifiedDate: datetime, connectorParameters: list[ConnectorParameter], Connectorcontenttypelinks: list[ConnectorContentTypeLink], DestinationId: str, Destinationpath: str):
        pass


class Target:
    def __init__(self, _id: str, name: str, parentTargetId: str, parentTargetPath: str, path: str, baseFolderId: str, baseFolderPath: str, outputExtension: str, cssClasses: str, cssFileId: str, cssFilePath: str, cssFileRecycled: bool, serializationType: SerializationType, Includexmldeclaration: bool, Includetargetpath: bool, removeBaseFolder: bool, useScheduledPublishing: bool, scheduledPublishDestinationMode: ScheduledDestinationMode, scheduledPublishDestinations: list[Identifier], timeToPublish: time, choice: Union[PublishIntervalHours, PublishDaysOfWeek, CronExpression], sendReportToUsers: str, sendReportToGroups: str, sendReportOnErrorOnly: bool, children: ContainerChildren):
        pass


class Template:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], TargetId: str, targetPath: str, formatId: str, FormatPath: str, formatRecycled: bool, xml: str, pageRegions: list[PageRegion]):
        pass


class TextBlock:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, text: str):
        pass


class Transportcontainer:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, children: ContainerChildren):
        pass


class Twitterfeedblock:
    def __init__(self, _id: str, name: str, parentFolderId: str, parentFolderPath: str, path: str, lastModifiedDate: datetime, lastModifiedBy: str, createdDate: datetime, createdBy: str, siteId: str, siteName: str, tags: list[Tag], metadata: Metadata, metadatasetId: str, metadatasetPath: str, reviewOnSchedule: bool, reviewEvery: int, expirationFolderId: str, expirationFolderPath: str, expirationFolderRecycled: bool, Accountname: str, Searchstring: str, Maxresults: int, Usedefaultstyle: bool, Excludejquery: bool, Querytype: TwitterQueryType):
        pass


class Unpublishparameters:
    def __init__(self, unpublish: bool, destinations: list[Identifier]):
        pass


class User:
    def __init__(self, Username: str, Fullname: str, Email: str, Authtype: UserAuthTypes, Password: str, Enabled: bool, Groups: str, Role: str, DefaultsiteId: str, Defaultsitename: str, Ldapdn: str):
        pass


class UserGroupIdentifier:
    def __init__(self, name: str, _type: EntityType):
        pass


class WordpressConnector:
    def __init__(self, _id: str, name: str, parentContainerId: str, parentContainerPath: str, path: str, siteId: str, siteName: str, auth1: str, auth2: str, url: str, verified: bool, verifiedDate: datetime, connectorParameters: list[ConnectorParameter], Connectorcontenttypelinks: list[ConnectorContentTypeLink]):
        pass
