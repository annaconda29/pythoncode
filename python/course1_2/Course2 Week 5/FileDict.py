#Test 1
#count = dict()
#print("Enter a line of text:")
#line = input(" ")
#words = line.split()
#print("Words:", words)
#print("Counting. . .")
#for word in words:
    #count[word] = count.get(word, 0) + 1
#print("Counts", count)

 #Test 2

name = input("Enter filename: ")
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print("The most common word is:", "'",bigword,"'", "and it appears",bigcount,"times")

