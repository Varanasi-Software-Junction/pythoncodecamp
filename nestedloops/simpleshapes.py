"""
oooo
oooo
oooo
oooo
Analysis
nrows=4
row     number of o's=nrows
1       4
2       4
3       4
4       4
"""
nrows = 4
for row in range(1, nrows + 1):
    for col in range(1, nrows + 1):
        print("o", end="")
    print()

"""
o
oo
ooo
oooo
Analysis
nrows=4
row     number of o's = row
1       1
2       2
3       3
4       4
"""
nrows = 4
for row in range(1, nrows + 1):
    for col in range(1, row + 1):
        print("o", end="")
    print()
"""
---o
--oo
-ooo
oooo
Analysis
nrows=4
row     number of spaces(nrows-row)     number of o's=row
1       3                                 1
2       2                                 2
3       1                                 3
4       0                                 4
"""
nrows = 4
for row in range(1, nrows + 1):
    for space in range(1, nrows - row + 1):
        print("-", end="")
    for col in range(1, row + 1):
        print("o", end="")
    print()
