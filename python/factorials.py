num = int(input("Enter number to calculate factorial: "))
factorial = 1

if num == 0:
    print("The factorial of 0 is 1")
elif num > 0:
    for x in range(1, num + 1):
        factorial = factorial * x
    print("The factorial of", num, "is", factorial)  

elif num < 0:
    for x in range(1, num + 1):
        factorial = factorial * x
    print("The factorial of", num, "is", factorial)     
        





