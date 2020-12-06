import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
lst1 = list()
lst2 = list()
url = input("Enter url: ")
fhand = urllib.request.urlopen(url).read()

tree = ET.fromstring(fhand)

count = tree.findall('.//count')


#print(lst1)
for x in count:
   lst2.append(int(x.text))
print(sum(lst2))

