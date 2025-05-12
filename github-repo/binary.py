#i wrote this thing for fun then found out python supported binary. accomplished the same thing with 1 line of code -_-

import sys

def main():
    try:
        decimal=binary_to_decimal(input('Binary: '))
    except ValueError:
        sys.exit('All characters must be 1 or 0')
    print('Decimal:',decimal)

def binary_to_decimal(binary):
    if type(binary)!=str:
        raise TypeError('Input must be string')
    binary=binary.strip()
    decimal=0
    power=len(binary)-1
    for i in binary:
        if i not in '10':
            raise ValueError('All characters must be 1 or 0')
        decimal+=int(i)*2**power
        power-=1
    return decimal

if __name__=='__main__':
    main()
