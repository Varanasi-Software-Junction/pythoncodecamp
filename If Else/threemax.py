from random import randint as rnd
a, b, c = rnd(1, 10), rnd(1, 10), rnd(1, 10)
print("a =", a, "b =", b, "c =", c)
# Method 1
if a >= b and a >= c:
    max = a
elif b >= c:
    max = b
else:
    max = c
print("Max =", max)

# Method 2
if a >= b:
    if a >= c:
        max = a
    else:
        max = c
else:
    if b >= c:
        max = b
    else:
        max = c
print("Max =", max)

# Method 3
if a < b or a < c:
    if b >= c:
        max = b
    else:
        max = c
else:
    max = a
print("Max =", max)


# Method 4
max = a
if b > max:
    max = b
if c > max:
    max = c
print("Max =", max)
