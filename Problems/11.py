
def isFib(x):

    a=0
    b=1
    if x==a:
        return True
    if x==b:
        return True
    n=2
    while(b<x):
        t=a+b
        a=b
        b=t
        #print(b)
        n += 1
    if x == b:
        return True
    return False

for i in range(0,20):
    print(i,isFib(i))