l = [x * 2 for x in range(10) if x < 9]
print(l)
r = range(1, 11)
l = list(r)
print(l)
l = [x for x in r if x % 2 == 0]
print(l)

l = [x ** 3 for x in r if x % 2 == 0]
print(l)
