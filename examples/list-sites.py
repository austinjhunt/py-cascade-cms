from ..cascadecms.driver import CascadeCMSRestDriver
import json


def disable_require_workflow_on_base_folder_of_all_sites():
    """ Loop through all sites in CMS and turn off requireWorkflow and for base folder. 
    This will solve the error message described here: https://www.hannonhill.com/cascadecms/latest/faqs/common-errors/workflow-is-required.html
    if you are dealing with sites that do NOT use workflow but whose root folders are set to require workflow. 
    Per Meg's advice from Hannon Hill (Support Specialist)
    1. get a list of sites with listSites
    2. for each site, perform a read operation on the siteId to 
        get the site's rootFolderId
    3. then use editWorkflowSettings on that root folder to set 
        requireWorkflow to false and applyRequireWorkflowToChildren to true 
    """
    driver = CascadeCMSRestDriver(
        organization_name="my-org", api_key='my-api-key', verbose=True)
    sites = driver.list_sites()['sites']
    for s in sites:
        site_asset = driver.read_asset(
            asset_type='site', asset_identifier=s['id'])
        site_name = site_asset['asset']['site']['name']
        root_folder_id = site_asset['asset']['site']['rootFolderId']
        # First store the current workflow settings in case you need to roll back
        root_folder_workflow_settings = driver.read_asset_workflow_settings(
            asset_type='folder',
            asset_identifier=root_folder_id
        )
        with open(f'data/folders/{root_folder_id}.json', 'w') as f:
            if driver.workflows_exist(root_folder_workflow_settings):
                driver.info(f'WORKFLOWS EXIST FOR SITE {site_name}')
            json.dump(root_folder_workflow_settings, f)

        # update existing workflow settings
        new_root_folder_workflow_settings = root_folder_workflow_settings['workflowSettings']
        new_root_folder_workflow_settings['requireWorkflow'] = False
        edit_workflow_payload = {
            'workflowSettings': new_root_folder_workflow_settings,
            'applyRequireWorkflowToChildren': True,
        }
        response = driver.edit_asset_workflow_settings(
            asset_identifier=root_folder_id, asset_type='folder', payload=edit_workflow_payload)
        with open(f'data/workflow-edit-responses/{root_folder_id}.json', 'w') as f:
            json.dump(response, f)


if __name__ == "__main__":
    disable_require_workflow_on_base_folder_of_all_sites()
