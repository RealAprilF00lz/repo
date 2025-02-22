s=input('camel case: ')
for i in s:
    if i.isupper():
        s=s.replace(i,'_'+i.lower())
print('snake case: '+s)
