n = 5
for row in range(1, n ):

    for star in range(1, row + 1):
        print("0", end="")
    for space in range(1,2*(n-row) + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        print("0", end="")

    print()
for row in range( n-2,-0,-1):

    for star in range(1, row + 1):
        print("0", end="")
    for space in range(1,2*(n-row) + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        print("0", end="")

    print()
