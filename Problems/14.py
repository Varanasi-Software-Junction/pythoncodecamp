def isPerCube(n):
    x = n**(1/3)
    x= x+0.5
    x = int(x)
    if x**3==n:
        return True
    return False
"""    x = 2
    while True:
        y = n / (x * x)
        if (x == y):
            print(x)
            if x == int(x):
                return True
            else:
                return False
        x = (y + x + x) / 3
        print(x)"""

print(isPerCube())