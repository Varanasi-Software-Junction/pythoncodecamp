count = 0


def createBoard():
    row = [0 for i in range(9)]
    board = [row.copy() for i in range(10)]
    return board


def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end="")
        print()


# board = createBoard()
# printBoard(board)

def isValidArray(a):
    freq = [0 for i in range(11)]
    n = len(a)
    for i in a:
        if i < 0 or i > 9:
            return False
        if i == 0:
            continue
        freq[i] += 1
        if freq[i] > 1:
            return False
    return True


def colToArray(board, colno):
    a = []
    for i in range(9):
        a.append(board[i][colno])
    return a


def boxToArray(board, rowno, colno):
    rowlimit = (rowno // 3 + 1) * 3# 0-2 =1, 3-5=2, 6-8 = 3
    collimit = (colno // 3 + 1) * 3
    a = []
    for i in range(rowlimit - 3, rowlimit):
        for j in range(collimit - 3, collimit):
            a.append(board[i][j])
    return a

    # print(row,c,end="   ,")


def isBoardFilled(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True


def isBoardValid(board):
    for i in range(9):
        if not isValidArray(board[i]):
            return False
        if not isValidArray(colToArray(board, i)):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isValidArray(boxToArray(board, i, j)):
                return False
    return True


def solve(board, i, j):
    global count
    for v in range(1, 10):
        board[i][j] = v
        # print(i, j,v, isBoardValid(board))
        if not isBoardValid(board):
            continue
        # printBoard(board)
        # input()
        if i == 8 and j == 8:
            count += 1
            print(count, " )")
            #printBoard(board)
            #input()
        else:
            if j < 8:
                solve(board, i, j + 1)
            else:
                solve(board, i + 1, 0)
    board[i][j] = 0


board = createBoard()
solve(board, 0, 0)
printBoard(board)
print(count)