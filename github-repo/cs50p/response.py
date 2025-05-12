from validators import email

if email(input('Email: '))==True:
    print('Valid')
else:
    print('Invalid')
