data1 = input("Enter any text to be sliced: ")
data2 = input("Enter the part which you want to start slicing (1 letter before that character):-  ")
data3 = input("Enter the character on which you want to end the slicing")
print("This is your text:", data1)
print("This is you starting position for slicing:", data2)
print("You want to slice until:", data3)
x = input("Are the following statments true or false? ")
pos1 = data1.find(data2)
pos2 = data1.find(data3)
print("Postion no. of first letter is", pos1)
print("Postion no. of second letter is", pos2)
if x == "True":
    slictxt = data1[pos1+1:pos2]
    print("Your sliced text, Your majesty:- ", slictxt)
if x == "False":
    print("Sorry, We are unable to slice your text.")    
    
    

