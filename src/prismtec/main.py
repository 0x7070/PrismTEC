import requests
import json

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': '98.235.155.235',
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': '46734023e7372cbcfbc9ebad8ee4e92ee29a93963c65e9ced1781743dc08722212afa0dbbe5bc317'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
print(json.dumps(decodedResponse, sort_keys=True, indent=4))