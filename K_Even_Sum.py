n = 11
k = 3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
total = sum(a[:k]) % 2
counteven = 0
if total % 2 == 0:
    counteven += 1
print(total)
for i in range(k, n):
    total = total + (a[i]%2) - (a[i - k]%2)
    print(total)
    if total % 2 == 0:
        counteven += 1
print("Even count = ", counteven)
