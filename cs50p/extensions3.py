mimetypes={
        '.gif':'image/gif',
        '.jpg':'image/jpeg',
        '.jpeg':'image/jpeg',
        '.png':'image/png',
        '.pdf':'application/pdf',
        '.txt':'text/plain',
        '.zip':'application/zip',
        }
fn=input("Filename: ").casefold().rstrip()
for e in mimetypes:
    if fn.endswith(e):
        print(mimetypes[e])
        quit()
print('application/octet-stream')

