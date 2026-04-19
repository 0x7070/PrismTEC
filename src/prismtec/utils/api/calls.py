from prismtec.utils.general.helpers import hrx, hr, clean
from prismtec.utils.general.indicators import is_ip

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

def query(url: str, headers: dict = None, parameters: dict = None) -> str:
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

def query_virustotal(indicator: None, indicator_type: str = 'ip'):
    indicator_type = clean(indicator_type)
    
    BASE_URL = None
    HEADERS = None
    PARAMETERS = None
    
    if indicator_type == 'ip':
        if not is_ip(indicator):
            raise ValueError(f'Indicator({type(indicator)}) `{indicator}` not a valid IPaddress.')
        
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
    return dump

def query_abuseipdb(indicator: None, indicator_type: str = 'ip') -> str:
    indicator_type = clean(indicator_type)
    
    BASE_URL = None
    HEADERS = None
    PARAMETERS = None
    
    if indicator_type == 'ip':
        if not is_ip(indicator):
            raise ValueError(f'Indicator({type(indicator)}) `{indicator}` not a valid IPaddress.')
        
        BASE_URL = 'https://api.abuseipdb.com/api/v2/check'
        INDICATOR = indicator
        
        # can pass many different parameters based on intended usage
        PARAMETERS = {
            'ipAddress': INDICATOR
        }
        HEADERS = {
            'Key': get_api_key(service='AbuseIPDB'),
            'Accept': 'application/json'
        }
        
    dump = query(
        url=BASE_URL,
        headers=HEADERS,
        parameters=PARAMETERS
    )
    return dump
    

#===

if __name__ == '__main__':
    hr()
    print(f'{MODULE_NAME} is loaded.')
    hr()
    
    # x = query_virustotal(
    #     indicator='33.31.58.46'
    # )
    # print(x)
    # hrx()
    aipdb = query_abuseipdb(
        indicator='99.12.13.4'
    )
    print(aipdb)
    
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