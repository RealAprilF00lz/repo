#it's called copycat.py because it's a copy of the cat command. get it? hahahahahahahaha i'm so funny

import sys

for i in sys.argv[1:]:
    try:
        with open(i) as file:
            print(file.read(),end='')
    except FileNotFoundError:
        print(f'cat: {i}: No such file or directory')
    except IsADirectoryError:
        print(f'cat: {i}: Is a directory')
    except PermissionError:
        print(f'cat: {i}: Permission denied')
