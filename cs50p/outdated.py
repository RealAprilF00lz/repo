months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input('Date: ')
        if date.find('/')==-1:
            m,d,y=date.strip().replace(',','').title().split()
            if m in months:
                m=str(months.index(m)+1)
                if int(m)<=12 and int(d)<=31:
                    break
        else:
            m,d,y=date.replace(' ','').split(sep='/')
            if int(m)<=12 and int(d)<=31:
                break
    except ValueError:
        pass
print(y,m.zfill(2),d.zfill(2),sep='-')


