#program to extract things from clipboard, inspired by automate the boring stuff with python by al sweigart

import re,clipboard,sys

def main():
    text=clipboard.paste()
    if len(sys.argv)<2:
        sys.exit('Missing command line argument')
    match sys.argv[1]:
        case 'email':
            matches=email(text)
            name='email adddresses'
        case _:
            sys.exit('Invalid command line argument')
    if len(matches)==0:
        sys.exit(f'No {name} found')
    clipboard.copy('\n'.join(matches))

def email(text):
    pattern = re.compile(r'''
    [a-zA-Z0-9._%+-]+ # Username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # Domain name
    (?:\.[a-zA-Z]{2,4}) # TLD
    ''',re.VERBOSE)
    return pattern.findall(text)

#TODO: add support for extracting other things

if __name__=='__main__':
    main()
