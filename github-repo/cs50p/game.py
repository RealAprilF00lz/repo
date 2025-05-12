from random import randint


def main():
    n=get_pos_int('Level: ')
    answer=randint(1,n)
    while True:
        guess=get_pos_int('Guess: ')
        if guess>answer:
            print('Too large!')
        elif guess<answer:
            print('Too small!')
        else:
            print('Just right!')
            break


def get_pos_int(prompt):
    while True:
        try:
            n=int(input(prompt))
            assert n>0
            return n
        except (ValueError, AssertionError):
            print('Please input a positive integer')


main()
