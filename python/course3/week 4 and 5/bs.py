import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#input section
url = input("Enter url: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

#repeat the procedure for "count" times
for i in range(count):
    # open a socket connection to the server, send a request and get the response data
    html = urllib.request.urlopen(url).read()
    # parse the received response data hello, why do we need to parse?
    # the received response is of type HTML
    # from this HTML, we 
    # need to "extract" <a href="<next url>"> ... ok ?
    #purpose of beautiful soup is to parse html? 
    soup = BeautifulSoup(html, 'html.parser')
    # collect all the "tags" in the response data named <a>
    tags = soup('a')

    #from the response received look for "pos" link.
    #have a counter to look for the "pos"
    j = 0
    for tag in tags:
        #skip pos-1 links because we only want the "pos" link
        j+=1
        #when we find the "pos" link - assign it to the url to read next
        if j == pos:
            #look for ref attribute which will be the next URL
            url = tag.get(('href'))
            print(url)
            break