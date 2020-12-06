numlist = list()
total = 0
count = 0
while True:
    inp = input("Enter a number: (type DONE(ALL CAPS) to exit)")
    if inp == 'DONE':
        break
    value = float(inp)
    numlist.append(value)
avg = sum(numlist) / len(numlist)

print("Average of entered numbers in list is:", avg)

x = list(range(5))
print(x)