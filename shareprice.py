prices = [2, 20, 5, 10, 8, 25, 80]
forwardmaxgain = []
print(prices)
n = len(prices)
for i in range(1, n + 1):
    forwardmaxgain += [max(prices[:i]) - min(prices[:i])]

print(forwardmaxgain)
