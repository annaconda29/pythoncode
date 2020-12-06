#Iter function in python
fruits = ("apple", "banana", "cherry")
myit = iter(fruits)
for x in range(3):
    print(next(myit))


mystr = "banana"
myit1 = iter(mystr)
for x in range(len(mystr)):
    print(next(myit1))







