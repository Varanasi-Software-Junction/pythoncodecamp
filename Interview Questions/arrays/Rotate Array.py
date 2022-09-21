a = [1, 2, 3, 4, 5, 6]
d = 3
part1 = a[:d]
part2 = a[d + 1:]
print(part1, part2)
rotated = part2 + part1
print(rotated)
