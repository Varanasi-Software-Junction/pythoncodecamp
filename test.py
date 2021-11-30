# Program to find all digits of a number

n = 123
sum = 0
while n > 0:
    rem = n % 10
    n //= 10
    sum += rem * rem

print(sum)

# End program
