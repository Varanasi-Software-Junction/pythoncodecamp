def bitcount(n):
    count = 0
    while n > 0:
        count = count + 1
        print(bin(n), bin(n - 1))
        n = n & (n - 1)
    return count


print(bitcount(256))
