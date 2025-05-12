def main():
    time=convert(input('What\'s the time? '))
    if time>=7 and time<=8:
        print('It\'s breakfast time')
    elif time>=12 and time<=13:
        print('It\'s lunch time')
    elif time>=18 and time<=19:
        print('It\'s dinner time')

def convert(time):
    hours,minutes=time.split(':')
    time=int(hours)+int(minutes)/60
    return time

if __name__ == "__main__":
    main()

