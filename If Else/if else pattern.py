a = 3
b = 1
c = 2
max = a if a >= b else b
print(max)
max = (a if a >= c else c) if a >= b else (b if b >= c else c)
print(max)
