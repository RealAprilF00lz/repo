def main():
    x=convert(input('Fraction: '))
    print(gauge(x))


def convert(fraction):
    try:
        x=round(eval(fraction)*100)
    except (NameError,SyntaxError):
        raise ValueError
    if x>100:
        raise ValueError
    return x


def gauge(percentage):
    if percentage<=1:
        return 'E'
    if percentage>=99:
        return 'F'
    return str(percentage)+'%'


if __name__ == "__main__":
    main()

