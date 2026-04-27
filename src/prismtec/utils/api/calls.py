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
        
        # Can pass many different parameters based on intended usage
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

def query_ipinfo(indicator: None, indicator_type: str = 'ip', fields: list = ['ip']) -> None:
    try:
        import ipinfo
    except ImportError:
        print('ERROR:\n- Module `ipinfo` is NOT INSTALLED. Skipping this query...')
        return None
    
    indicator_type = clean(indicator_type)
    
    if indicator_type == 'ip':
        if not is_ip(indicator):
            raise ValueError(f'Indicator({type(indicator)}) `{indicator}` not a valid IPaddress.')
        
        handler = ipinfo.getHandlerLite(access_token=get_api_key(service='ipinfo'))
        details = handler.getDetails(indicator)
        
        attributes = {}
        for field in fields:
            attributes.update({field: getattr(details, field)})
            
        return attributes

def query_shodan(indicator: None, indicator_type: str = 'ip', facets: list = None) -> None:
    try:
        import shodan
    except ImportError:
        print('ERROR:\n- Module `shodan` is NOT INSTALLED. Skipping this query...')
        return None
    
    indicator_type = clean(indicator_type)
    
    if indicator_type == 'ip':
        if not is_ip(indicator):
            raise ValueError(f'Indicator({type(indicator)}) `{indicator}` not a valid IPaddress.')
        
        SHODAN_API_KEY = get_api_key(service='shodan')
        api = shodan.Shodan(key=SHODAN_API_KEY)
        host_information = api.host(indicator)
        return host_information

#===

if __name__ == '__main__':
    hr()
    print(f'{MODULE_NAME} is loaded.')
    hr()
    

    # host_info = query_shodan(
    #     indicator='8.8.8.8'
    # )
    # print(host_info)
    
    # attributes = query_ipinfo(
    #     indicator='33.31.58.46',
    #     fields=[
    #         'ip',
    #         'as_name'
    #     ]
    # )
    # print(attributes)
    
    # x = query_virustotal(
    #     indicator='33.31.58.46'
    # )
    # print(x)
    
    # aipdb = query_abuseipdb(
    #     indicator='99.12.13.4'
    # )  
    # print(aipdb)
