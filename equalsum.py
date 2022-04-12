

Numbers = [i for i in range(1, 10)]
Maximum = 9

Array = [0 for i in range(0, Maximum + 1)]
Array[0] = 1

for CurrentNum in Numbers:
    for Num in range(Maximum - CurrentNum, -1, -1):
        if (Array[Num]):
            Array[Num + CurrentNum] += Array[Num]

print(Array[Maximum])