fn=input('File name: ').rstrip().casefold()
if fn.endswith('.gif'):
    print('image/gif')
elif fn.endswith('.jpg') or fn.endswith('.jpeg'):
    print('image/jpeg')
elif fn.endswith('.png'):
    print('image/png')
elif fn.endswith('.pdf'):
    print('application/pdf')
elif fn.endswith('.txt'):
    print('text/plain')
elif fn.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')
