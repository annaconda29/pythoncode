print("This will tell you your name in ASCII (American Standard Code for Information Interchange)")
name = input("What is your name: ")
print(name)
for x in name:
    print(ord(x))