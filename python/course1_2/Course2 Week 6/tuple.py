c = {'b': 1, 'c': 2, 'a': 3}

for k, v in sorted(c.items()):
    print(k,v)



tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)

print(tmp)