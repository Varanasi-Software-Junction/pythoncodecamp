def nextPalin(n):
    l = len(str(n))
    # print(l)
    divider = 10 ** (l // 2)
    # print(divider)
    if l % 2 == 0:
        firstpart = n // divider
        secondpart = n % divider
    else:
        firstpart = n // (divider * 10)
        secondpart = n % divider

    firstpart = int(str(firstpart)[::-1])
    # print(firstpart, secondpart)
    diff = firstpart - secondpart
    # print(diff)
    # print(n + diff)
    result = n + diff
    if result > n:
        return result
    else:
        return nextPalin(n + 10 - (n % 10))


x = 34521
print(nextPalin(x))
