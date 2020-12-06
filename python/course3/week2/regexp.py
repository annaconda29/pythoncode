import re
fhand = open('hp.txt')
for line in fhand:
    line = line.rstrip()
    if re.search("The", line):
        print(line)