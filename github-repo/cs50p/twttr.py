s=input('Input: ')
vowels='aeiou'
for i in s:
    j=i.lower()
    if j in vowels:
        s=s.replace(i,'')
print('Output:',s)
