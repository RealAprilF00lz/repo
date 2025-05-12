import sys
import csv

if len(sys.argv)<3:
    sys.exit('Too few arguments')
if len(sys.argv)>3:
    sys.exit('Too many arguments')

try:
    with open(sys.argv[1]) as file:
        r=csv.DictReader(file)
        j=[]
        for i in r:
            last,first=i['name'].replace(' ','').split(',')
            j.append({'first':first,'last':last,'house':i['house']})
except (FileNotFoundError,KeyError):
    sys.exit('File could not be read')

with open(sys.argv[2],'w') as file:
    writer=csv.DictWriter(file,fieldnames=['first','last','house'])
    writer.writeheader()
    for i in j:
        writer.writerow(i)
