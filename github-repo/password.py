import re

def main():
    print('Is your password strong enough?')
    result=check(input('Password: ').strip())
    print(result)

def check(p):
    if len(p)>=8:
        if re.search(r'[a-z].*[A-Z]',p):
            if re.search(r'\d',p):
                return True
    return False

if __name__=='__main__':
    main()
