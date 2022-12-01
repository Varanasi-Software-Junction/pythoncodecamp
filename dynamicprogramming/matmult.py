def printMatrix(m):
    n = len(m)
    for i in (range(1, n)):
        for j in reversed(range(i, n)):
            r = m[i][j]
            print(r, end="\t")
        print()


p = [30, 35, 15, 5, 10, 20, 25]
inf = 10000000000000
n = len(p)
x = [0 for x in range(n)]
m = [x.copy() for i in range(n)]

for i in range(1, n):
    m[i][i] = 0

for length in range(2, n):
    for i in range(1, n - length + 1):
        j = i + length - 1
        m[i][j] = inf
        for k in range(i, j):
            q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
            if q < m[i][j]:
                m[i][j] = q

printMatrix(m)
minsteps=m[1][-1]
print(minsteps)