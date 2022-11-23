a = [1, 2, 3, 4, 5]
n = len(a)
print(n)
n = 3
mid = n // 2
print(mid)
print(a)
start = 2
for i in range(mid):
    a[i + start], a[start + n - 1 - i] = a[start + n - 1 - i], a[start + i]
print(a)
