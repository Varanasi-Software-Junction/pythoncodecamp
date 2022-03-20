def f(n):
    count = 0
    for x in n:
        count += x
    return count


a = [(1, 2, 3), (1, 1, 1), (2, 5, 4), (0, 1, 0)]
print(a)
a.sort(key=f)
print(a)
