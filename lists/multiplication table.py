n = 3
table = []
for i in range(1, 11):  # Via a loop
    table.append(n * i)
print(table)
table = [n * x for x in range(1, 11)]  # List comprehension
print(table)
