a = [2, 4, 6, 7,9]
b = [1, 2, 3, 5, 8]
n1 = len(a)
n2 = len(b)
c = [0] * (n1 + n2)
i, j, k = 0, 0, 0
while i <= n1 - 1 and j <= n2 - 1:
    if a[i] <= b[j]:
        c[k] = a[i]
        i += 1
    else:
        c[k] = b[j]
        j += 1
    k += 1
print(c)
for p in range(i, n1):
    c[k] = a[p]
    k += 1
for p in range(j, n2):
    c[k] = b[p]
    k += 1
print(c)
