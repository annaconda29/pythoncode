# importing math Module
import math

#sqrt() method
x = int(input("Type a number "))
print("The Square root of", x, "is", math.sqrt(x))

#math.ceil, math.floor
y = float(input("Type a number to round to the highest number "))
z = float(input("Type a number to round to the lowest number "))
print(y, "rounded to the highest number is", math.ceil(y))
print(z, "rounded to the highest number is", math.floor(z))

# prints pi
a = math.pi
print("Pi:", a)