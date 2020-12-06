import urllib.request, urllib.parse, urllib.error
lst = list()
from bs4 import BeautifulSoup
url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')
for tag in tags:
    spantag = tag.text
    intspan = int(spantag)
    
    app = lst.append(intspan)
sum = sum(lst)
print(sum)