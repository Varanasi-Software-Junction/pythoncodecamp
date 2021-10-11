a = [2, 4, 9, 6, 1, 7, 5, 2, 1, 2]
print(a)
f = [0 for x in range(10)]
print(f)
for x in a:
    f[x] += 1
print(f)
for i in range(1, 10):
    f[i] += f[i - 1]
print(f)
output = [0 for x in a]
print(output)
for i in reversed(range(len(a))):
    value = a[i]
    pos = f[value] - 1
    output[pos] = value
    f[value] -= 1
print(output)
