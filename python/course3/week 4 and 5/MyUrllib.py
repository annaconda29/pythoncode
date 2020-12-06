import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('')
for line in fhand:
    print(line.decode().strip())
