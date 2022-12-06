def printMatrix(m, mrow, mcol):
    pass



def findPath(a, y, x, mrow, mcol, destx, desty,steps):
    if y < 0 or y >= mrow:
        return
    if x < 0 or x >= mcol:
        return
    if x == destx and y == desty:
        return
    if a[y][x] != 1:
        return


grid = [[1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]]
source = [0, 1]
destination = [2, 2]
