def pascal(y,x):
    print(y,x)
    if x==1:
        return 1
    if y==x:
        return 1
    return pascal(y-1,x) +pascal(y-1,x-1)

