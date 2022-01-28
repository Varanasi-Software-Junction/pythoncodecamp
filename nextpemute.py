a = [1, 2, 3, 6, 7, 5, 4]
n = len(a)
i = n - 1
while i > 0 and a[i] <= a[i - 1]:
    i -= 1
print(i)