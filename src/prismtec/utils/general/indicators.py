from prismtec.utils.general.helpers import hr, hrx
import ipaddress

__all__ = [
    '',
]

#===

def is_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
        
#===Main
if __name__ == '__main__':
    print('indicators package LOADED')
    hrx()
    
    print(is_ip('10.0.0.1'))