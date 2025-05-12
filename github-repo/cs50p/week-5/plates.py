def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<=6 and len(s)>=2:
        if s[0].isalpha() and s[1].isalpha():
            if s.isalnum():
                if s.rstrip('1234567890').isalpha():
                    if s[s.find('0')-1].isdigit() or s.find('0')==-1:
                        return True
    return False


if __name__ == "__main__":
    main()

