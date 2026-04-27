__all__ = [
    'hr',
    'hrx'
]

#===
def hr(char: str = None, size: int = None) -> None:
    if char is None:
        char = '-'
    if size is None:
        size = 30
    print(f'{char*size}')
    
def hrx() -> None:
    """
    `hrx` -- Horizontal Rule 2.

    Large horizontal rule

    Args:
        NA

    Returns:
        NA
    
    Raises:
        NA

    Example:
        >>> hrx()
        expected_output:
        ```
    
        ====================
        
        ```
    """
    print()
    hr(
        char='=',
        size=80
    )    
    print()
    
def clean(string: str, funcs = None) -> str:
    if not funcs:
        funcs = [str.strip, str.lower]
        
    for func in funcs:
        string = func(string)
        
    return string
    
def title(string: str = None, char: str = None, width: int = None,
           spaces: int = None, return_val: bool = None) -> str:
    if char is None:
        char = '~'
    if width is None:
        width = 80
    if spaces is None:
        spaces = 5
    if string is None:
        string = 'default'
    if return_val is None:
        return_val = False

    formatting = [
        str.strip,
        #str.title
    ]
    for func in formatting:
        #print(f'PRE  {func.__name__}: `{string}`')
        string = func(string)
        #print(f'POST {func.__name__}: `{string}`')
        #_hr()

    string = f'{' '*spaces}{string}{' '*spaces}'
    string = f'{string:{char}^{width}}'

    if return_val:
        return string
    else:
        print(string)
        
        
def msg(msg_loc: str = None, msg_str: str = None,
         msg_sym: chr = None, msg_typ: str = None,
         acc_msg: str = None) -> str:
    acceptable_msg_types = ['WARN', 'ERROR', 'EXCEPTION']
    if msg_typ not in acceptable_msg_types:
        msg(
            msg_loc ='_msg func',
            msg_str = f'msg_type `{msg_typ}` not in {acceptable_msg_types}. Defaulting to `WARN`',
            msg_typ = 'WARN'
        )

    if msg_sym is None:
        if msg_typ == 'ERROR':
            msg_sym = '!'
        if msg_typ == 'WARN':
            msg_sym = '*'
        if msg_typ == 'EXCEPTION':
            msg_sym = '#'

    if msg_loc is None:
        msg_loc = 'GENERAL_LOC'

    if msg_str is None:
        msg_str = 'GENERAL_MSG'
    else:
        msg_str = f'\n[{msg_sym}] {msg_typ}:\n  - `{msg_loc}`:\n  -- {msg_str}\n'
    if acc_msg is not None:
        msg_str += f' -- {acc_msg}\n'

    print(msg_str)
        
#===Main
if __name__ == '__main__':
    print('helpers package LOADED')