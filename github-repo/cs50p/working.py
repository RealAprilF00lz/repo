import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match=re.search(r'([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([0-9]|1[0-2])(:[0-5][0-9])? (AM|PM)',s)
    if match==None:
        raise ValueError
    if match.group(3)=='PM':
        hr1=int(match.group(1))+12
    else:
        hr1=match.group(1)
    if match.group(6)=='PM':
        hr2=int(match.group(4))+12
    else:
        hr2=match.group(4)
    min1=match.group(2)
    if min1==None:
        min1=':00'
    min2=match.group(5)
    if min2==None:
        min2=':00'
    return f'{hr1}{min1} to {hr2}{min2}'


if __name__ == "__main__":
    main()

