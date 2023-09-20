# candor-py
Python Library for Candor Services' Project Mercury API.

## Documentation
`candor.py` requires Python 3.8 or higher.
You can add the library to your project with:
```
pip install candor
```
https://pypi.org/project/candor/

Your public API key can be found at https://dashboard.candorservices.net/api-dashboard.

### Verifying a license
You can verify if a license is valid using this function:
```py
valid = verifyLicense(PUB_API_KEY, LICENSE_KEY, PRODUCT_ID);
```

You'll want to grab your product ID from https://dashboard.candorservices.net/license-manager by creating a new product and then adding a license. The license key should be added by the client, using some sort of config (we recommend remote configs, see below!). Assign your license to your client using the tools in the dashboard.

### Retrieving a remote config
Remote configs allow clients to easily configure parts of their apps without having to mess with complicated or messy configuration files. You can use this function:
```py
obj = candor.getConfig(PUB_API_KEY, CONFIG_ID);
```
to retrieve the remote config as an object. You can create a remote config at https://dashboard.candorservices.net/config-manager.

## Need support?
If you need help with anything to do with this project, then please see the [project-mercury-support](https://discord.com/channels/650773903236399134/1146431646418079744) channel in Discord under the FREELANCERS category.