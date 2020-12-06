x = str(input("Enter Filename: "))
try:
    fname = open(x, "r")
except:
    print("File:", x, "cannot be opened", "Your fault :(")
    quit()

print("This program prints the file & prints the character count (till a given place in the file) ")
print("It also prints line count and prints lines that only start with given phrase")

print("No. 1: File content printing:")
fname = open(x)
for line in fname:
    print(line)
print("File printing done!!!")



print("No. 2: Character count")
fname = open(x)
fcount = fname.read()
wcount = len(fcount)
print("Your file has", wcount, "characters")
word = int(input("Enter a number within the given value above that you want to find character count: "))
abc = fcount[:word]
print("Character Count:     ", abc, "     ", "that is the number of characters till",  word)
print("Character Count printing done!!!")

print("No.3: Line count")
fname = open(x)
count = 0
for line in fname:
    count = count + 1
print("There are", count, "lines in your file." )
print("Line Count printing done!!!")

print("No. 4: Printing lines that only start with given phrase/prompt")
fname = open(x)
for line in fname:
    print(line)
print("The following is the content of the file")
fname = open(x)
phr = input("What is the starting phrase:   ")
count = 0
for line in fname:
    line = line.rstrip()
    if line.startswith(phr):
        count = count + 1
print("There are", count, "number of", phr, "lines in your file")