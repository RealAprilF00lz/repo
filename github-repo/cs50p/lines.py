import sys

if len(sys.argv)<2:
    sys.exit('Too few arguments')
if len(sys.argv)>2:
    sys.exit('Too many arguments')
if not sys.argv[1].endswith('.py'):
    sys.exit('Not a python script')
try:
    file=open(sys.argv[1])
except FileNotFoundError:
    sys.exit('File does not exist')

lines=0
for i in file:
    if not i.lstrip().startswith('#') and not i.isspace():
        lines+=1
print('Lines:',lines)
file.close()
