result = []


def findsum(n, currentnumbers, currentsum):
    print("Calling ", n, currentnumbers, currentsum)
    if n <= 0:
        return

    if currentsum < 0:
        return

    if currentsum == 0:
        result.append(currentnumbers)
        return

    findsum(n, currentnumbers + [n], currentsum - n)
    findsum(n - 1, currentnumbers, currentsum)


n = 4
findsum(n, [], n)
print(result)
