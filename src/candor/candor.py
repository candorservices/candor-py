import requests

def verifyLicense(api_key: str, license_key: str, product_id: str):
    data = {
        'product_id': product_id,
        'key': license_key
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key
    }
    response = requests.post("https://dashboard.candorservices.net/api/licenses/verify", json=data, headers=headers)

    if response.status_code == 200:
        json_response = response.json()
        isLicenseValid = json_response.get('success', False)
        return isLicenseValid
    elif response.status_code == 401:
        json_response = response.json()
        error_code = json_response.get('code', None)
        if error_code == 0:
            raise ValueError("License key is not valid")
        elif error_code == 1:
            raise ValueError("Specified product doesn't exist")
        elif error_code == 2:
            raise ValueError("License key is not valid for specified product")
        elif error_code == 3:
            raise ValueError("License key had too many IPs")
        elif error_code == 4:
            raise ValueError("You don't own the specified product or license key")
        else:
            raise ValueError("License verification failed with an unknown error")
    elif response.status_code == 403:
        raise ValueError("API key is invalid")
    else:
        raise ValueError("License verification failed with an unknown error")

def getConfigs(api_key: str, config_id: str):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': api_key
        }
        response = requests.get(f"https://dashboard.candorservices.net/api/configs/{config_id}", headers=headers)
        json_response = response.json()
        values = json_response.get('values', {})
        return values
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch config information.")
        return {}