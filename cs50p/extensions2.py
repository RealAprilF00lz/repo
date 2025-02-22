def mime(fn,e,m):
    if fn.rstrip().casefold().endswith(e):
        print(m)
        quit()

fn=input('File name: ')
mime(fn,'.gif','image/gif')
mime(fn,'.jpg','image/jpeg')
mime(fn,'.jpeg','image/jpeg')
mime(fn,'.png','image/png')
mime(fn,'.pdf','application/pdf')
mime(fn,'.txt','text/plain')
mime(fn,'.zip','application/zip')
print('application/octet-stream')
