"""
---0
--00
-000
0000
---1
--12
-123   star =1,2,3, 1,2,3
1234
n=4
row     space    star
1       3           1
2       2           2
3       1           3
4       0           4
space=4-row, n-row,
star=row
---0
--000
-00000
0000000
---1
--121
-12321
1234321
---1
--12 1
-123 21
1234 321
1 to row and row-1 to 1
row         space       star
1           3           1
2           2           3
3           1           5
4           0           7
space =n-row
n=1,2,3,4,5
even = 2*n 2,4,6,8,10
odd=even-1=1,3,5,7,9, = 2*n-1
star =

"""
n = 4
for row in range(1, n + 1):
    for space in range(1, n - row + 1):
        print(" ", end="")
    for star in range(1, row + 1):
        print(star, end="")
    for star in reversed(range(1, row)):
        print(star, end="")
    print()
