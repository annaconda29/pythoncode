#place holder = curly braces {}
price = 49
txt = "This apple is {} dollars"
print(txt.format(price))

#place holder = {:.2f}
#Will print with 2 decimal places
price = 49
txt1 = "This apple is {:.2f} dollars"
print(txt1.format(price))

#Multiple place holders
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))