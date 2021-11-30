# Program to search for Happy Numbers


"""
A Happy Number is a number where the sum of digits squared s equal to 1 ultimately. What do we mean by ultimately?
The best way is to learn by an example.
Example
10 = 12 + 02 = 1 + 0=1. So 10 is a Happy Number

Let us try with 19
sum =12 + 92 = 1 + 81 = 82
sum=82 + 22 = 64 + 4 = 68
sum=62 + 82 = 36 + 64 = 100
sum= 12 + 02 + 02= 1 + 0 + 0 = 1
19 ultimately reaches 1 so it is a Happy Number.


"""

n = 18
ncopy = n
a = [n]
while True:
    sum = 0
    while n > 0:
        rem = n % 10
        n = n // 10
        sum += rem * rem
    if sum == 1:
        a += [sum]
        print(ncopy, " is a happy number")
        print(a)
        break
    if sum in a:
        a = a + [sum]
        print(ncopy, " is not a happy number")
        print(a)
        break
    a = a + [sum]
    n = sum

# End Program
