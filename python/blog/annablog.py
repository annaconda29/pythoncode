from BeautifulSoup import BeautifulSoup

fmt1 = "<li><a href=\""
fmt2="\"><img src=\""
fmt3="\"/></a>"
fmt4 ="</li>"


infile = open("in.html", "r")
textfromblogger = infile.read()
outfile1 = open("out1.html", "r")
out1 = outfile1.read()
outfile2 = open("out2.html", "r")
out2 = outfile2.read()
outfile3 = open("out3.html", "r")
out3 = outfile3.read()
outfile = open("out.html", "w")


sp = BeautifulSoup(textfromblogger)
a = sp.findAll('a', href=True);
texts = sp.findAll("div", {"class":"separator"});


outfile.write(out1)
j = 0
start = 0
for i in range(len(texts)):
    if(len(texts[i].text) > 6):
        if(start==0):
            outfile.write(texts[i].text)
            start = 1
            outfile.write(out2)
            continue
        else:
            try:
                outfile.write(fmt1 + a[j]['href'] + fmt2 + a[j]['href'] + fmt3 + texts[i].text +fmt4)
                j=j+1
            except IndexError:
                print ''
outfile.write(out3)
