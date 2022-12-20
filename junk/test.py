a = [1, 2, 1, 2, 5]
frequencies = {}
for item in a:
    value = frequencies.get(item)
    if value is None:
        frequencies[item] = 1
    else:
        frequencies[item] += 1
# print(frequencies)
a.clear()
for item in frequencies:
    if frequencies[item] == 1:
        a.append(item)
print(a)
