n = 5

for row in range(n,0,-1):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row+1 ):
        print("0 ", end="")
    print()

for row in range(2, n +1):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row+1 ):
        print("0 ", end="")
    print()
