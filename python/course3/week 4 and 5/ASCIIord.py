x = int(input("HOW MANY LETTERS ARE THERE IN YOUR NAME: "))
lst = list()
for letter in range(x):
    inp = input("Enter each letter of your name as the prompt appears in capital or lowercase: ")
    y = ord(inp)
    print("ASCII:", y)
    lst.append(y)
print("Your name in ASCII: ", lst)
 
