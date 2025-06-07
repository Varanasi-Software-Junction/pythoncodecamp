def prime_generator(n):

    primes = [2, 3, 5]
    # n = 100
    t = 2
    nextprimecandidate = 5
    nextprimecandidate += t
    while True:
        isprime = True
        sqrtlimit = int(nextprimecandidate)
        for p in primes:
            if p > sqrtlimit:
                isprime = True
                break
            if nextprimecandidate % p == 0:
                isprime = False
                break
        if isprime:
            primes.append(nextprimecandidate)
        t = 6-t
        nextprimecandidate += t
        if len(primes) >= n:
            # print(primes)
            return primes
result=prime_generator(15)
print(result)