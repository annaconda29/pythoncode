print("Hi Vaishu! I made this game for you. Hope you like it!!!")
print("Count the sum with your toys and have fun")
points = 0
#First Question
q1 = int(input("What is 2 + 3: "))
if q1 == 5:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")

#Second Question
q2 = int(input("What is 3 + 6: "))
if q2 == 9:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Third Question
q3 = int(input("What is 2 + 2: "))
if q3 == 4:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Fourth Question
q4 = int(input("What is 1 + 1: "))
if q4 == 2:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Fifth Question
q5 = int(input("What is 1 + 3: "))
if q5 == 4:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Sixth Question
q6 = int(input("What is 2 + 1: "))
if q6 == 3:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Seventh Question
q7 = int(input("What is 3 + 3: "))
if q7 == 6:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Eight Question
q8 = int(input("What is 9 + 1: "))
if q8 == 10:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Ninth Question
q9 = int(input("What is 5 + 2: "))
if q9 == 7:
    print("Very Good!!")
    points = points + 1
else:
    print("Wrong :(")
#Tenth Question
q10 = int(input("What is 3 + 5: "))
if q10 == 8:
    print("Very Good!!")
    points = points + 1


print("You scored", points, "/ 10")


if points == 10:
    print("All Correct. YAAAAAAAY!!!")
if points > 4:
    print("You passed!!!!")
elif points < 4:
    print("You failed :(")


