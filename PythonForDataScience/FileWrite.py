with open("Ex2.txt", "w") as File1:
    x = 1
    for x in range(10):
        
        File1.write("This is line ")
        File1.write(str(x))
        File1.write("\n")
        x = x + 1
print("Done")