import urllib.request, urllib.parse, urllib.error
lst = list()
from bs4 import BeautifulSoup

url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for tag in tags:
    x = tag.get('span')
    y = int(x)
    z = sum(y)
    print(z)
    lst.append(z)
print(lst)
