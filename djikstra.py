def printMatrix(a):
    n = len(a)
    print("\t\t", end="")
    for i in range(n):
        print("\t\t" + str(chr(ord('A') + i)), end="")
    print()
    line = 0
    for row in a:
        print("\t\t" + str(chr(ord('A') + line)), end="")
        line += 1
        for item in row:
            print("\t\t" + str(item), end="")
        print()


def min(x, y):
    if x <= y:
        return x
    else:
        return y


def dJikstra(a):
    n = len(a)
    minpos = 1
    for i in range(1, n):
        if a[0][i] < a[0][minpos]:
            minpos = i
    # print(minpos)
    for i in range(1, n):
        a[0][i] = min( a[0][i] , a[0][minpos] + a[minpos][i])


inf = float("inf")

dist = [[inf, 10, inf, 5, inf], [inf, inf, 1, 2, inf], [inf, inf, inf, inf, 4], [inf, 3, 9, inf, 2],
        [7, inf, 6, inf, inf]]
printMatrix(dist)
dJikstra(dist)
print()
printMatrix(dist)
