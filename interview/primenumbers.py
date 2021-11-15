# Program to find all prime numbers up to a limit


primeLimit = 500  # Find prime numbers to this limit
innerLoopRuns = 0  # Count the runs of the inner loop
count = 0  # Variable where the count of primes found will be stored
primes = []  # List in which primes will be stored
print("2,3,", end="")  # 2 and 3 are prime numbers. Print it
count += 2  # Increment prime count by 2
t1 = 2
for n in range(5, primeLimit + 1,
               t1):  # Run a loop from 2 to the required limit. Start at 3 and increment by 2. Odd numbers only
    t1 = 6 - t1
    if n % 3 == 0:  # Check for division by 3 and go back and generate another number if divisible by 3
        continue
    limit = int(n ** 0.5)  # Limit to which divisors need to be checked
    isPrime = True  # Assume the number to be prime
    t2 = 2
    for divisor in range(5, limit + 1, t2):  # Run a loop to the limit
        t2 = 6 - t2
        innerLoopRuns += 1
        if n % divisor == 0:  # Check whether the remainder upon division is 0
            isPrime = False  # If remainder is 0 then the number isn't prime
            break  # If it isn't prime then break the loop
    if isPrime:
        print(n, end=",")
        count += 1  # Prime found. Increment the count
print("\nPrimes Count=", count)
print("\nInner loop runs is ", innerLoopRuns)

# End program
