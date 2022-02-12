def bitCount(n):
    s = bin(n)
    print(s)
    s = s.replace("0", "")

    n = len(s)
    return n - 1


print(bitCount(10))
