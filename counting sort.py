a = [4, 3, 5, 5, 6, 1]
n = len(a)
b = [0 for i in range(n)]
freq = [0 for i in range(10)]
print(a)
print(freq)
for i in a:
    freq[i] += 1
for i in range(1, 10):
    freq[i] += freq[i-1]
print(freq)
for i in range(n-1, -1, -1):
    value = a[i]
    pos = freq[value]
    freq[value] -= 1
    b[pos-1] = value

print(b)
