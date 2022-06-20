def table(n):
    for i in range(1, 11):
        yield n * i


for x in table(7):
    print(x)
a = [x for x in table(6)]
print(a)
