a1 = [1,2,3]
a1 = set(a1)
a1 = list(a1)
b1 = [2,4,6]
c = []
d = []
e = []
for i in a1:
    if i not in b1:
        d.append(i)
for i in b1:
    if i not in a1:
        e.append(i)
c.append(d)
c.append(e)
print(c)