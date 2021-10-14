def addList(l):
    sum = 0
    for i in l:
        sum += i
    return sum


def average(l):
    sum = addList(l)
    n = len(l)
    return sum / n


def sublist(l, value):
    newlist = []
    for x in l:
        newlist = newlist + [x - value]
    return newlist


def multiplylist(l1, l2):
    newlist = []
    n = len(l1)
    for i in range(0, n):
        x = l1[i]
        y = l2[i]
        newlist = newlist + [x * y]
    return newlist


x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
sumx = addList(x)
sumy = addList(y)
# print(sumx)
# print(sumy)

avgx = average(x)
avgy = average(y)
# avgy=4.5
print("x-Mean", avgx)
print("Y-Mean", avgy)

dx = sublist(x, avgx)
dy = sublist(y, avgy)
# print(dx)

# print(dy)

sigmadx = addList(dx)
sigmady = addList(dy)
print("sigmadx=", sigmadx)
print("sigmady", sigmady)
dxdy = multiplylist(dx, dy)
# print(dxdy)
dxdx = multiplylist(dx, dx)
# print(dxdx)
dydy = multiplylist(dy, dy)
# print(dydy)
sigmadxdy = addList(dxdy)
print("sigmadxdy", sigmadxdy)
sigmadxdx = addList(dxdx)
sigmadydy = addList(dydy)

print("sigmadxdx", sigmadxdx)
print("sigmadydy", sigmadydy)
n = len(x)
num = (sigmadxdy - sigmadx * sigmady / n)
print("num", num)
den = (sigmadxdx - sigmadx * sigmadx / n)
print("den", den)
regressionsoefficient = num / den
print("coeff", regressionsoefficient)
xvalue = 7
yvalue = avgy + regressionsoefficient * (xvalue - avgx)
print("yvalue", yvalue)
