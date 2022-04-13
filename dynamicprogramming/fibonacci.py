def fib(n):
    global count
    count += 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def dpFib(n):
    global count
    global fibs
    count += 1
    if fibs.get(n) is None:
        fibs[n] = dpFib(n - 1) + dpFib(n - 2)  # Memoize
    return fibs[n]


fibs = {}

count = 0
result = fib(10)
print(result, end=",")
print(count)
count = 0
fibs = {1: 0, 2: 1}
result = dpFib(10)
print(result, end=",")
print(count)
print(fibs)
