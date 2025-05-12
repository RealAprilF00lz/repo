import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match=re.fullmatch(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})',ip)
    if match==None:
        return False
    for i in match.groups():
        if int(i)>255:
            return False
    return True


if __name__ == "__main__":
    main()

