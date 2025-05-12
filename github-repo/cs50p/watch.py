import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s=re.search(r'<iframe.*src=.*youtube\.com/embed/(.+?)"',s)
    if s==None:
        return s
    return 'https://youtu.be/'+s.group(1)


if __name__ == "__main__":
    main()

