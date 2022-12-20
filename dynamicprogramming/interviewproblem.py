def printMatrix(mat):
    for i in mat:
        for j in i:
            print(j, end='  ')
        print()


def isValid(y, x, maxy, maxx):
    # In this function check valid condition
    if y < 0 or x < 0:
        return False
    if y >= maxy or x >= maxx:
        return False
    return True


def makeMove(mat, y, x, path, max_y, max_x):
    # In this function move the matrix path
    """
    dir=1 forward
    dir=2 down
    dir=3 back
    """
    if y == max_y - 1 and x == max_x - 1:
        print("Solved", path)  # print the matrix solved path
        path.pop()  # pop solving path
        return
    print(path)

    new_x = x + 1  # Dir=1 forward
    if isValid(y, new_x, max_y, max_x):
        if mat[y][new_x] == 0:
            mat[y][new_x] = 2
            path.append((y, new_x))
            makeMove(mat, y, new_x, path, max_y, max_x)
    new_x = x - 1  # Dir=3 back
    if isValid(y, new_x, max_y, max_x):
        if mat[y][new_x] == 0:
            mat[y][new_x] = 2
            path.append((y, new_x))
            makeMove(mat, y, new_x, path, max_y, max_x)
    new_y = y - 1  # Dir=4 down
    if isValid(new_y, x, max_y, max_x):
        if mat[new_y][x] == 0:
            path.append((new_y, x))
            mat[new_y][x] = 2
            makeMove(mat, new_y, x, path, max_y, max_x)

    if len(path) > 0:
        path.pop()


m = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1],
     [1, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1]]
n = len(m)
printMatrix(m)
path = [(2, 3)]

solvedpaths = []
makeMove(m, 2, 3, path, 5, 6)
