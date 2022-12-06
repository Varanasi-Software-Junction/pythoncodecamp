def printMatrix(mat):
    for i in mat:
        for j in i:
            print(j, end='  ')
        print()


m = [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 1]
n = len(m)
printMatrix(m)
start = [0, 0]  # y,x
end = [n - 1, n - 1]  # y,x
starty = start[0]
startx = start[1]
endy = end[0]
endx = end[1]
# 0^ 1> 2 neeche 3<

dir = 0
y = starty
x = startx
count = 2
m[y][x] = count

while True:
    if y == endy and x == endx:
        print("Solved")
        break
    dir = (dir + 1) % 4
    print("dir", dir, "sy", y, "sx", x)
    if dir == 1:
        newx = x + 1
        if newx >= n:
            continue
        if m[y][newx] == 0:
            continue
        x = newx
        count += 1
        m[y][x] = count
        dir = (dir + 2) % 4
        printMatrix(m)
        input()
        continue
    if dir == 2:
        newy = y + 1
        if newy >= n:
            continue
        if m[newy][x] == 0:
            continue
        y = newy
        count += 1
        m[y][x] = count
        dir = (dir + 2) % 4
        printMatrix(m)
        input()
        continue
    if dir == 3:
        newx = x - 1
        if newx < 0:
            continue
        if m[y][newx] == 0:
            continue
        x = newx
        count += 1
        m[y][x] = count
        dir = (dir + 2) % 4
        printMatrix(m)
        input()
        continue
    if dir == 0:
        newy = y - 1
        if newy < 0:
            continue
        if m[newy][x] == 0:
            continue
        y = newy
        count += 1
        m[y][x] = count
        dir = (dir + 2) % 4
        printMatrix(m)
        input()
        continue




