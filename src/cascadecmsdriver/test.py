from config import *


def get_content_manager_emails_from_site_name(site_name):
    group = driver.read_asset(asset_type='group', asset_identifier=site_name)
    print(group)


def get_widget_xml_from_site(siteName):
    url = f'https://cofc.cascadecms.com/api/v1/read/page/{siteName}/content/widget?{auth}'
    response = driver.session.get(url)
    return response.json()


def get_sites_missing_widgets():
    sites = driver.list_sites()
    sites_missing_widgets = []
    for s in sites:
        name = s['path']['path']
        site_id = s['id']
        widget = get_widget_xml_from_site(name)
        if 'message' in widget and ".cofc.edu" in name:
            msg = widget['message']
            if "Unable to identify an entity based on" in msg:
                sites_missing_widgets.append(site_id)
    return sites_missing_widgets


def copy_asset_to_site_content_folder(asset_id: str = '', asset_type: str = 'page', asset_name: str = '', site: dict = None) -> dict:
    """ Copy an asset to a site's content folder """
    content_folder = driver.read_asset(
        asset_type='folder', asset_identifier=f'{site["path"]["path"]}/content'
    )
    if 'asset' in content_folder:
        content_folder = content_folder['asset']['folder']
    else:
        return {site["path"]["path"]: 'skip'}
    print(f'Asset Name: {asset_name}')
    print(
        f'Copying asset id {asset_id} of type {asset_type} to destination content folder id {content_folder["id"]} with new name {asset_name}')
    response = driver.copy_asset_to_new_container(
        asset_identifier=asset_id,
        asset_type=asset_type,
        new_name=asset_name,
        destination_container_identifier=content_folder["id"]
    )
    return response


def copy_asset_to_all_sites(asset_type: str = 'page', asset_id: str = ''):
    """ Given an asset id, copy it to the content folder of all sites in CMS. """
    sites = driver.list_sites()['sites']
    print(f'Sites: {sites}')
    asset = driver.read_asset(asset_type=asset_type, asset_identifier=asset_id)
    for s in sites[2:]:
        # Get the content folder.
        response = copy_asset_to_site_content_folder(
            asset_id=asset_id,
            asset_type=asset_type,
            asset_name=asset['asset'][asset_type]['name'],
            site=s)
        print(response)
        break


if __name__ == '__main__':
    # get_content_manager_emails_from_site_name('testweb.cofc.edu')
    # response = driver.unpublish_asset(
    #     asset_type='page', asset_identifier='683e85e7ac1e0009144ab6f40f913af4')
    # print(response)
    # page = driver.read_asset(
    #     asset_type='page', asset_identifier='680784d8ac1e0009144ab6f44f9a794b')
    # print(page)

    copy_asset_to_all_sites(
        asset_type='page', asset_id='88783c24ac1e002e6d0e81020980e37a')
