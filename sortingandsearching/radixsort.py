def countingSort(a, pos):
    # print(a)
    f = [0 for x in range(10)]
    # print(f)
    for x in a:
        xpos = digit(x, pos)
        f[xpos] += 1
    # print(f)
    for i in range(1, 10):
        f[i] += f[i - 1]
    # print(f)
    output = [0 for x in a]
    # print(output)
    for i in reversed(range(len(a))):
        value = a[i]
        vpos = digit(value, pos)
        npos = f[vpos] - 1
        output[npos] = value
        f[vpos] -= 1
        # print(output)
        # print(f)
    return output


def digit(n, pos):
    for i in range(pos - 1):
        n = n // 10
    return n % 10


a = [124, 95, 167, 249, 305]
print(a)
n = 3
for i in range(1, n + 1):
    a = countingSort(a, i)
    print(a)
print(a)
