# multiplication of a and b without using multiply
a = int(input())
b = int(input())
sign = 1
if a < 0 and b >= 0 or b < 0 and a >= 0:
    sign = -1
if a < 0:
    a = -a
if b < 0:
    b = -b
if a < b:
    counter = a
    number = b
else:
    counter = b
    number = a
result = 0
while counter > 0:
    result += number
    counter -= 1
if sign < 0:
    print(-result)
else:
    print(result)
