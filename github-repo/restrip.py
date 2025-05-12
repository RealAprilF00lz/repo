import re

def strip(s,chars=' \t\n'):
    s=re.sub(f'^[{chars}]+','',s)
    s=re.sub(f'[{chars}]+$','',s)
    return s
