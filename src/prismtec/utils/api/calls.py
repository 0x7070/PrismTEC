from prismtec.utils.general.helpers import hrx, hr, clean
import requests, json

__all__ = [
    'hr',
    'hrx'
]

#===
MODULE_NAME = 'prismtec.utils.api.calls'

#===

#buildurl, query, dump_json, parse_json

def build_url(base_url: str, params: list) -> str:
    temp_url = base_url
    if temp_url[-1] == '/':
        temp_url = temp_url[:-1]
    
    for param in params:
        temp_url += f'/{param}'
    return temp_url

def query(url: str, headers: dict = None, parameters: dict = None) -> requests.models.Response:
    RESPONSE = requests.get(
        url=url,
        headers=headers,
        params=parameters
    )
    
    dump = dump_json(RESPONSE=RESPONSE)
    return dump

def get_api_key(service: str) -> str:
    service = clean(service)
    
    with open('CONFIG.json', 'r') as file:
        data = json.load(file)
        api_key = data['API-keys'][service]
        file.close()
        
    return api_key    

def dump_json(RESPONSE: requests.models.Response) -> str:
    decoded_response = json.loads(RESPONSE.text)
    dump = json.dumps(obj=decoded_response,
               sort_keys=True,
               indent=4)
    return dump
    
#----------------

def query_virustotal(indicator: None, type: str = 'ip'):
    type = clean(type)
    
    BASE_URL = None
    HEADERS = None
    PARAMETERS = None
    
    if type == 'ip':
        BASE_URL = 'https://www.virustotal.com/api/v3/ip_addresses'
        INDICATOR = indicator
        URL = build_url(base_url=BASE_URL,
                        params=[INDICATOR])
        
        HEADERS = {
            'accept': 'application/json',
            'x-apikey': get_api_key('VirusTotal')
        }
    
    dump = query(
        url=URL,
        headers=HEADERS,
        parameters=PARAMETERS
    )
    print(dump)

#===

if __name__ == '__main__':
    hr()
    print(f'{MODULE_NAME} is loaded.')
    hr()
    
    query_virustotal(
        indicator='33.33.33.33'
    )
    
# import requests
# import json

# # Defining the api-endpoint
# url = 'https://api.abuseipdb.com/api/v2/check'

# querystring = {
#     'ipAddress': '98.235.155.235',
#     'maxAgeInDays': '90'
# }

# headers = {
#     'Accept': 'application/json',
#     'Key': '46734023e7372cbcfbc9ebad8ee4e92ee29a93963c65e9ced1781743dc08722212afa0dbbe5bc317'
# }

# response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# # Formatted output
# decodedResponse = json.loads(response.text)
# print(json.dumps(decodedResponse, sort_keys=True, indent=4))