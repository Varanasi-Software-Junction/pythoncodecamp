def fastzerosum():
    a = [1, 2, 3, -4]
    a.sort()
    print(a)


def zerosum():
    a = [1, 2, 3, -4]
    n = len(a)
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                x = a[i]
                y = a[j]
                z = a[k]
                total = x + y + z
                if total == 0:
                    return 1
        return 0


print(fastzerosum())
