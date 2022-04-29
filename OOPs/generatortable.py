def table(n):
    i = 1
    while i <= 10:
        yield i * n
        i += 1


tbl = table(5)
for x in tbl:
    print(x)
