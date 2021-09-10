def printBoard(board):
    for b in board:
        print(b)
moves=set()
def horseMove(board,x,y):
    if x < 1 or x > 8 or y < 1 or y > 8:
        return
    t=(x,y)
    if t in moves:
        return
    moves.add(t)
    board[x-1][y-1]=1
    print(x,y)
    horseMove(board,x + 1,y +  2)
    horseMove(board,x + 1, y - 2)
    horseMove(board,x + 2, y + 1)
    horseMove(board,x + 2, y - 1)
    horseMove(board,x - 1,y +  2)
    horseMove(board,x - 1, y - 2)
    horseMove(board,x - 2, y + 1)
    horseMove(board,x - 2, y - 1)





board =[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
#printBoard(board)
horseMove(board,1,1)
printBoard(board)