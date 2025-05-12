from sys import argv
from random import choice
from pyfiglet import Figlet
figlet=Figlet()

if len(argv)==3:
    if argv[1] not in ['-f','--font']:
        quit('Invalid option')
    if argv[2] not in figlet.getFonts():
        quit('Invalid font')
    input=input('Input: ')
    figlet.setFont(font=argv[2])
    print(figlet.renderText(input))
elif len(argv)==1:
    input=input('Input: ')
    random_font=choice(figlet.getFonts())
    figlet.setFont(font=random_font)
    print(figlet.renderText(input))
else:
    print('Wrong number of arguments')
