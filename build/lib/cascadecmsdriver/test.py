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


if __name__ == '__main__':
    get_content_manager_emails_from_site_name('testweb.cofc.edu')
    response = driver.unpublish_asset(
        asset_type='page', asset_identifier='683e85e7ac1e0009144ab6f40f913af4')
    print(response)
    page = driver.read_asset(
        asset_type='page', asset_identifier='680784d8ac1e0009144ab6f44f9a794b')
    print(page)
