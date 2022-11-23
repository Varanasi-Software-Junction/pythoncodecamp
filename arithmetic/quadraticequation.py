a, b, c = 1, 2, -3
print(a, b, c)
d = b * b - 4 * a * c
d = d ** 0.5
r1 = (-b + d) / (2 * a)
r2 = (-b - d) / (2 * a)
print("r1=", r1, ",r2=", r2)
