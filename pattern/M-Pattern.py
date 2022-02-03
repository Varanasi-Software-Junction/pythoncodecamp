n = 7
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if col==1 or col==n or row<=n//2+1 and( row == col or row+col==n+1):
            print("0", end="")
        else:
            print(" ", end="")
    print()
