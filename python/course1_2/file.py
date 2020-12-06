#xfile = open("file1.txt")
#print(xfile)
#for x in xfile:
    #print(x)

xfile = open("file1.txt")
count = 0
for line in xfile:
    count = count +1
print("Line count:", count)


xfile = open("file1.txt")
x = xfile.read()
print(x)
print(len(x))
y = x[:209]
print(y)

xfile = open("file1.txt")
for line in xfile:
    line = line.rstrip()
    if not line.startswith("Her "):
        continue
    print (line)
    

