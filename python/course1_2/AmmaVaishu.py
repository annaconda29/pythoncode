#str1 = 'Hello Amma'
#print(str1)
#print(str1.lower())
#print(str1.upper())
#str2 = 'Hello Annu'
#print(str2)
#print(str2.replace('Annu','Vaishu!'))
#str3 = 'Hello Sanjeev'
#print(str3)
#print(str3.replace('e', 'X'))

import string

def alphalist(name):
    list1 = list(string.printable)
    print(list1)
    i = 0
    while i < len(name):
        for alpha in list1:
            print(alpha, alpha in name)
        i += 1

alphalist("Sanjeev")


