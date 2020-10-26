#!/bin/env python

def list_add_and_str(list, i=0):
    '''for each member of the given list, add i and convert to string'''
    return [str(e + i) for e in list]

def unwrap(s: str) -> str:
    '''return s without the first and last character'''
    return ''.join(s[1:-1])

def stringis_list(s:str):
    '''string represents a list'''
    return s[0] == '[' and s[-1] == ']'

def stringis_string(s:str):
    '''string represents a string'''
    return (s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'")

def stringis_int(s:str):
    '''string represents an integer'''
    try:
        int(s)
        return True
    except ValueError:
        return False

def stringis_float(s:str):
    '''string represents an floating-point number'''
    try:
        float(s)
        return True
    except ValueError:
        return False

def unstring(s: str):
    '''convert the string representation of a variable back into the original variable'''
    s = s.strip()
    if stringis_list(s):
        return [unstring(e) for e in unwrap(s).split(',')]
    if stringis_string(s):
        return unwrap(s)
    if strings_int:
        return int(s)
    if strings_float:
        return float(s)
    return s





def main():
    pass

if __name__ == "__main__":
    main()

