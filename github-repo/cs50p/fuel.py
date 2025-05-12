while True:
    try:
        x=round(eval(input('Fraction: '))*100)
        if x>100:
            print('Numerator cannot be greater than denominator')
            continue
        break
    except ZeroDivisionError:
        print('Denominator cannot be 0')
    except (NameError,SyntaxError):
        print('Please input a fraction')
if x<=1:
    quit('E')
if x>=99:
    quit('F')
print(str(x)+'%')

