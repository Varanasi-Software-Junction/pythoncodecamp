# range(start=0, end, step=1)
# range(10) start=0, end=10, step =1 and it will run from start to end-1, 0 to 9
# 1,2,3,,,,8,9,10
def printRange(r):
    print(r)
    for i in r:
        print(i, end=",")
    print()


printRange(range(11))
printRange(range(1, 11))
printRange(range(1, 11, 2))
printRange(range(10, 1))
printRange(range(10, 0, -1))
printRange(reversed(range(11)))
