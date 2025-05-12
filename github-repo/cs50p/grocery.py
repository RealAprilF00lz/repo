x={}
try:
    while True:
        y=input().upper().strip()
        if y not in x:
            x.update({y:1})
        else:
            x[y]+=1
except EOFError:
    print('')
    for i in sorted(x):
        print(x[i],i)
