prices = [2, 30, 15, 10, 8, 25, 80]
forwardmaxgain = []
backwardmaxgain = []
print(prices)
n = len(prices)
for i in range(1, n + 1):
    forwardmaxgain += [max(prices[:i]) - min(prices[:i])]

print(forwardmaxgain)
for i in range(n, -1, -1):
    if len(prices[i:]) == 0:
        continue
    backwardmaxgain = [max(prices[i:]) - min(prices[i:])] + backwardmaxgain
print(backwardmaxgain)
