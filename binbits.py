for i in range(101):
    l=[int(x) for x in bin(i)[2:]]
    if sum(l)==3:
        print(l,i)
