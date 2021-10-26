a = [4, -2, 6, 0, 23]
minpos = 0
maxpos = 0
n = len(a)
for pos in range(1, n):
    if a[pos] > a[maxpos]:
        maxpos = pos
    elif a[pos] < a[minpos]:
        minpos = pos
print("Min pos={0}, maxpos={1}, difference={2}".format(minpos, maxpos, maxpos - minpos))
