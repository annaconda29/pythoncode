import numpy as numpy 
num = numpy.random.randint(100)
chance = 10
for x in range(10):
    guess = int(input("Enter Number from 1 to 100: "))
    if guess == num:
        print("Correct")
        break
    elif guess > num:
        print("Too large")
    elif guess < num:
        print("Too small")
    chance = chance - 1
    print("You have ", chance, " chances left.")
print("It is ", num)
