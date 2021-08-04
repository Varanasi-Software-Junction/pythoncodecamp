n=99999
t=n
while(t//10!=0):
    x=t
    sum=0
    while(x!=0):
        sum += x%10
        x=x//10
    t=sum
    print(sum)
