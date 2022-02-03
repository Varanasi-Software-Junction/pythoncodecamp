n = 6
h = 2 * n - 1
for row in range(n, 0, -1):
    for star in range(1, row + 1):
        print("0", end="")
    for space in range(1, h - 2 * row):
        print(" ", end="")
    for star in range(1, row + 1):
        print("0", end="")
    print()
