"""
The Eight Queens Problem is a famous combinatorial problem in Computer Science where 8 queens
are to be placed on an 8 X 8 chess board such that no queens attach each other.


"""

n = 8
# The no of queens to be placed. The Chess Board will be N X N
count = 0
# Counts the no of solutions
placedqueens = [(0, 0)] * n


# A list to store the X,Y positions found by solving the problem


def printBoard():
    # Function that prints the solution board
    global placedqueens
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if (y, x) in placedqueens:
                # Check if the given x,y position has a placed queen
                print("\tQ", end="")
            else:
                if (y + x) % 2 == 0:
                    print("\tW", end="")
                else:
                    print("\tB", end="")
        print()


def isAttacked(queenNo, y, x):
    # Check if the given x,y position is under attack from any of the queens placed so far
    global placedqueens

    for i in range(queenNo - 1):
        py = placedqueens[i][0]
        px = placedqueens[i][1]
        if px == x:
            return True
        if py == y:
            return True
        if px + py == x + y:
            return True
        if px - py == x - y:
            return True
    return False


def placeQueens(queenno):
    # Place the queens
    global count
    global placedqueens
    y = queenno
    for x in range(1, n + 1):
        if isAttacked(queenno, y, x):
            continue
        placedqueens[queenno - 1] = (y, x)
        if queenno == n:
            # If n queens placed then update the count and print the result
            count += 1
            print(count, ")", placedqueens)
            printBoard()

        else:
            placeQueens(queenno + 1)
            # Place the next queen


placeQueens(1)
# Calling the function
