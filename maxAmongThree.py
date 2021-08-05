a = 67
b = 1006
c = 1002
"""if (a>=b and a>=c):
    print(a)
elif (b>=c and b>=a) :
    print(b)
elif (b>=a and b>=b) :
    print(c)"""
max=a
if a>=b:
    if b>=c:
        max =a
    else:
        if a>=c:
            max =a
        else:
            max = c
else:
    if a>=c:
        max =b
    else:
        if b>=c:
            max=a
        else:
            max=c
print(max)

