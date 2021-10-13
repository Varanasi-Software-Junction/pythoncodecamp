from matplotlib import pyplot as plt


def f(x, m, c):
    return m * x + c


x = [10, 20, 30]
y = [15, 10, 5]
sumx = sum(x)
sumy = sum(y)

n = len(x)
avgx = sum(x) / n
avgy = sum(y) / n
dx = [v - avgx for v in x]
dy = [v - avgy for v in y]

sigmadx = sum(dx)
sigmady = sum(dy)
dxdy = [dx[i] * dy[i] for i in range(n)]
# print(dxdy)
dxdx = [v * v for v in dx]
# print(dxdx)
dydy = [v * v for v in dy]
sigmadxdy = sum(dxdy)
sigmadxdx = sum(dxdx)
sigmadydy = sum(dydy)

n = len(x)
num = (sigmadxdy - sigmadx * sigmady / n)

den = (sigmadxdx - sigmadx * sigmadx / n)

m = num / den

c = avgy - m * avgx
inputx=[x for x in range(31)]
inputy=[f(x,m,c) for x in inputx]
print(m, c)
plt.scatter(x, y)
plt.plot(inputx,inputy)
plt.show()
