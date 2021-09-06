def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
#print(factorial(4))
def sumFact(n):
    sum = 0
    for i in range(n+1):
        sum += factorial(i)
    return sum
n=4
print(sumFact(n))

#sum =1
for i in range(0,n+1):
    if i==0:
        fact=1
        sum=1
        continue
    fact=fact*i
    sum=sum+fact
print(sum)
