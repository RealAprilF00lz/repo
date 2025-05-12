from random import randint


def main():
    level=get_level()
    correct_answers=0
    for _ in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        for i in range(3):
            answer=int(input(f'{x} + {y} = '))
            if answer!=x+y:
                print('EEE')
                if i==2:
                    print(f'{x} + {y} = {x+y}')
                    break
            else:
                correct_answers+=1
                break
    print(f'{correct_answers}/10 correct')


def get_level():
    while True:
        level=input('Level: ')
        if level in '123':
            return int(level)


def generate_integer(level):
    if level not in [1,2,3]:
        raise ValueError
    if level==1:
        return randint(0,9)
    elif level==2:
        return randint(10,99)
    else:
        return randint(100,999)


if __name__ == "__main__":
    main()

