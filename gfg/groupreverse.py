def groupReverse(a, left, right):
    n = right - left + 1
    mid = n // 2
    for i in range(mid):
        start = i + left
        end = n - 1 - i + left
        a[start], a[end] = a[end], a[start]


a = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
n = len(a)
parts = n // k
for i in range(1, parts + 1):
    start = (i - 1) * k
    end = i * k - 1
    groupReverse(a, start, end)
print(a)
