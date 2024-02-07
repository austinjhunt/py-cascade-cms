from cascadecmsdriver.driver import CascadeCMSRestDriver
from cascadecmsdriver.cmstypes import Identifier, CopyParameters, WorkflowConfiguration
from dotenv import load_dotenv
import os
import json
load_dotenv()
driver = CascadeCMSRestDriver(
    organization_name=os.environ.get('CASCADE_ORG'),
    api_key=os.environ.get('CASCADE_API_KEY'),
    verbose=False
)
sites = driver.listSites()['sites']
print(f'Total sites: {len(sites)}')
sites_with_trees = {}
sites_with_published_trees = {}
example_tree_id = driver.read_asset(
    asset_type='page', asset_identifier='88de92cdac1e002e6d0e81028e1ce3df')['asset']['page']['id']
for s in sites:
    basepath = f"{s['path']['path']}/content"
    site_id = s['id']
    has_tree = False
    has_published_tree = False
    treepath = f'{basepath}/tree'
    response = driver.read_asset(asset_type='page', asset_identifier=treepath)
    if 'asset' in response and 'page' in response['asset'] and response['asset']['page']['name'] == 'tree':
        has_tree = True

        if 'lastPublishedDate' in response['asset']['page'] and response['asset']['page']['lastPublishedDate'].startswith('202'):
            has_published_tree = True
        else:
            print(f'{basepath} tree not published')
    else:
        print(f'{basepath} missing tree')
    sites_with_trees[s['path']['path']] = has_tree
    sites_with_published_trees[s['path']['path']] = has_published_tree

    if not has_tree:
        # copy tree from another site to this site's content folder and publish.
        res = driver.read_asset(asset_type='folder', asset_identifier=basepath)
        if 'asset' in res:
            copy_to_folder_id = res['asset']['folder']['id']

            copyParams = CopyParameters(
                destinationContainerIdentifier=copy_to_folder_id, doWorkflow=False, newName='tree')

            copy_response = driver.copy(
                identifier=Identifier(example_tree_id, 'page'),
                copyParameters=copyParams, workflowConfiguration=WorkflowConfiguration(None, None, None, None, None, None))
            print(f'Copy response: {copy_response}')
    elif not has_published_tree:
        # publish the tree.
        pass

with open('sites_with_trees.json', 'w') as f:
    json.dump(sites_with_trees, f)

with open('sites_with_published_trees.json', 'w') as f:
    json.dump(sites_with_published_trees, f)
