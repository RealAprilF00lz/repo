from datetime import date
import sys
import inflect
p=inflect.engine()


def main():
    try:
        print(calculate(input('Date of birth (YYYY-MM-DD): ')))
    except ValueError:
        sys.exit('Invalid date format')


def calculate(d):
    d=date.fromisoformat(d)
    d=date.today()-d
    d=d.days*1440
    return f'{p.number_to_words(d,andword="")} minutes'


if __name__ == "__main__":
    main()

