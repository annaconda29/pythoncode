count = dict()
numbs = [1, 2, 3, 4]

for no in numbs:
    count[no] = count.get(no, 0) + 1
print(count)
