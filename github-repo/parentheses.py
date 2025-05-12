def main():
    print('This program will check whether all parentheses in the inputted text have a corresponding parenthesis.')
    print(check(input('Text: ')))

def check(s):
    x=0
    for i in s:
        if i=='(':
            x+=1
        if i==')':
            x-=1
        if x<0:
            return False
    if x==0:
        return True
    else:
        return False

if __name__=='__main__':
    main()
