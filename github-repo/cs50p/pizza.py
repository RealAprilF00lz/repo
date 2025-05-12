import sys
from tabulate import tabulate
import csv

if len(sys.argv)<2:
    sys.exit('Too few arguments')
if len(sys.argv)>2:
    sys.exit('Too many arguments')
if not sys.argv[1].endswith('.csv'):
    sys.exit('Not a CSV file')
try:
    file=open(sys.argv[1])
except FileNotFoundError:
    sys.exit('File does not exist')
table=csv.reader(file)
print(tabulate(table,tablefmt='grid'))
file.close()
