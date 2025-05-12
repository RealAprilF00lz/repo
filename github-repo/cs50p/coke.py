due=50
while due>0:
    print('Amount due:',due)
    coin=int(input('Insert coin: '))
    if coin==25 or coin==10 or coin==5:
        due-=coin
print('Change owed:',due*-1)
