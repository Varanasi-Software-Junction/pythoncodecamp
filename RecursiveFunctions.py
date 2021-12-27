def fibonacci(n):
    if n < 0:
        raise Exception("Invalid value for factorial " + str(n))
    return n - 1 if n <= 2 else fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    if n < 0:
        raise Exception("Invalid n = " + str(n))
    return 1 if n == 0 else n * factorial(n - 1)


print(fibonacci(5))
print(factorial(6))
