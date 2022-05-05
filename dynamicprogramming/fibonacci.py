



def fib(n):#Fib without DP
    global count
    count += 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def dpFib(n):#Fib with DP
    global count
    global fibs
    count += 1
    if fibs.get(n) is None:
        fibs[n] = dpFib(n - 1) + dpFib(n - 2)  # Memoize
    return fibs[n]


fibs = {}

count = 0
result = fib(6)
print("Fib(6) without Memoization ", result, ", count=", count)
count = 0
fibs = {1: 0, 2: 1}
result = dpFib(6)
print("Fib(6) with Memoization ", result, ", count=", count)
print("Dictionary as memo ", fibs)



