a = [1,5,0,1,6,4]
a.sort()
print(a)
n = len(a)
even = []
odd = []
for i in range(0, n):
    if i % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
odd.sort(reverse=True)
print(odd, even)
a.clear()
e = 0
o = 0
for i in range(n):
    if i % 2 == 0:
        a.append(even[e])
        e += 1
    else:
        a.append(odd[o])
        o += 1

print(a)
