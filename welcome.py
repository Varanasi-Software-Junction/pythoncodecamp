n = 11
m = 3 * n
# print(n,m)
mid = (n + 1) // 2
for row in range(1, mid):
    mid = 3 + 6 * (row - 1)
    side = (m - mid) // 2
    for dash in range(1, side + 1):
        print("-", end="")
    for star in range(1, mid//2 + 1):
        print(".|", end="")
    print(".", end="")
    for dash in range(1, side + 1):
        print("-", end="")
    print()
sidelength=(m-7)//2
for i in range(1,sidelength+1):
    print("-",end="")
print("WELCOME",end="")
for i in range(1,sidelength+1):
    print("-",end="")
print()
mid = (n + 1) // 2
for row in reversed(range(1, mid)):
    mid = 3 + 6 * (row - 1)
    side = (m - mid) // 2
    for dash in range(1, side + 1):
        print("-", end="")
    for star in range(1, mid//2 + 1):
        print(".|", end="")
    print(".", end="")
    for dash in range(1, side + 1):
        print("-", end="")
    print()
