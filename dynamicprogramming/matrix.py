def multiplymatrix(a, b):
    m = len(a)
    n = len(a[0])
    n1 = len(b)
    if n != n1:
        print("Error ")
        return None
    r = len(b[0])
    # mXn , nXr = mXr
    t = [0 for x in range(r)]
    result = [t.copy() for x in range(m)]

    for i in range(m):
        for j in range(n):
            for k in range(r):
                result[i][k] += a[i][j] * b[j][k]
    return result, m * n * r
def printmatrix(m):
    print()
    for row in m:
        for col in row:
            print("\t", col, end="")
        print()


m1 = [1, 2, 3], [4, 5, 6]
m2 = [1, 2], [3, 4], [5, 6]
printmatrix(m1)
printmatrix(m2)
c, steps = multiplymatrix(m1, m2)
printmatrix(c)
print(steps)
