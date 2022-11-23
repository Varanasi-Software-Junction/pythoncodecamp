def printMat(m):
    print()
    for r in m:
        print(r)
    print()


p = [30, 35, 15, 5, 10, 20, 25]
n = len(p)
# print(p)
# print(n)
m = [[1 for i in range(n)] for i in range(n)]
# printMat(m)
for i in range(n):
    m[i][i] = 0
printMat(m)
