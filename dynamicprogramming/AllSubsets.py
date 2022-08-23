combinations = []


def binaryNumbers(n):
    binaries = [0 for x in range(n)]
    # print(binaries)
    i = 0
    combinations.append(binaries.copy())
    while True:
        while i <= n - 1:
            if binaries[i] == 0:
                binaries[i] = 1
                combinations.append(binaries.copy())
                i = 0
                continue
            else:
                binaries[i] = 0
                i += 1
            if i > n - 1:
                return combinations


def allCombinations(a):
    pass


a = [10, 20, 5, 11, 13, 15]
print(a)
a = binaryNumbers(5)
print(a)
