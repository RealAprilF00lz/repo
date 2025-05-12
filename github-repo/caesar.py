import sys

def main():
    plain=input('Plaintext: ')
    try:
        key=int(input('Key: '))
    except ValueError:
        sys.exit('Key must be integer')
    print('Ciphertext:',caesar(plain,key))

def caesar(plain,key=1):
    cipher=''
    for i in plain:
        if i.isalpha():
            i=ord(i)
            if chr(i).isupper():
                while i+key>90:
                    i-=26
                i+=key
            if chr(i).islower():
                while i+key>122:
                    i-=26
                i+=key
            i=chr(i)
        cipher+=i
    return cipher
    
if __name__=='__main__':
    main()
