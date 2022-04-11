# Cascade CMS 8 REST API Python Driver

This is a module for simplifying interaction with [Hannon Hill's Cascade CMS 8 REST API](https://www.hannonhill.com/cascadecms/latest/developing-in-cascade/rest-api/index.html). This was built to handle some day-to-day task automation with Cascade CMS 8 for the College of Charleston but can be used / contributed to by anyone else using the content management system.

## Usage

```
# you can provide a username and password or alternatively an api key
# verbose boolean indicates whether to use verbose logging
driver = CascadeCMSRestDriver(
    organization_name="cofc", api_key='my-api-key', verbose=True)
sites = driver.list_sites()['sites']
for s in sites:
    asset = driver.read_asset(asset_type='site', asset_identifier=s['id'])
    driver.debug(asset)

```
