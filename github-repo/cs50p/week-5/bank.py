def main():
    greeting=input('Greeting: ').lstrip()
    print(value(greeting))


def value(greeting):
    x=greeting.lower()
    if x.startswith('hello'):
        return 0
    elif x.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

