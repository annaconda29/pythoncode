import re
x = "My Favourite numbers are 2 and 29 "
y = re.findall("[0-9]+", x)
print(y)
