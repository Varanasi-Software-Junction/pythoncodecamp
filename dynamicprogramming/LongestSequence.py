a = [10, 20, 5, 11, 13, 15]
n = len(a)
maxsize = 0
maxseq = []
a.append(a[n - 1] - 1)
# print(a)
n += 1
# print(n)
start = 0
for i in range(n - 1):
    if a[i + 1] < a[i]:
        # print(start, i)
        # print(a[start:i + 1])
        length = i - start + 1
        if length > maxsize:
            maxsize = length
            maxseq = a[start:i + 1]
        start = i + 1
print(maxseq)
