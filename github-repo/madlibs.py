import sys
import re

#open madlibs.txt, read the text, close madlibs.txt
try:
    file=open('madlibs.txt')
except FileNotFoundError:
    sys.exit('No madlibs.txt file found')
text=file.read()
file.close()

#find placeholder words and prompt user to replace them
matches=re.findall(r'(?:ADJECTIVE)|(?:NOUN)|(?:ADVERB)|(?:VERB)',text)
for i in matches:
    text=text.replace(i, input(f'Enter {i.lower()}: ').strip(), 1)

#print result and write it to madlibsresult.txt
print(text,end='')
with open('madlibsresult.txt','w') as file:
    file.write(text)
