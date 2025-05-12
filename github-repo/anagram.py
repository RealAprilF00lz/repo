def main():
    print('Is it an anagram?')
    text1=input('Text 1: ')
    text2=input('Text 2: ')
    print(isanagram(text1,text2))

def isanagram(text1,text2):
    text1,text2=text1.lower(),text2.lower()
    for i in text2:
        if not i.isalnum():
            text2=text2.replace(i,'')
    for i in text1:
        if i.isalnum():
            if i not in text2:
                return False
            text2=text2.replace(i,'',1)
    if text2=='':
        return True
    else:
        return False
        
if __name__=='__main__':
    main()
