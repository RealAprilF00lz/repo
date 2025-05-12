def main():
    print('Output:',shorten(input('Input: ')))


def shorten(word):
    vowels='aeiou'
    for i in word:
        j=i.lower()
        if j in vowels:
            word=word.replace(i,'')
    return word


if __name__ == "__main__":
    main()

