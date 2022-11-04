buildings = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(buildings)
maxheight = max(buildings)
print(maxheight)
lm = 0
rm = 0
n = len(buildings)
for i in range(1, n - 1):
    value = buildings[i - 1]
    if value > lm:
        lm = value
    t = (lm, value, i)
    print(t)
