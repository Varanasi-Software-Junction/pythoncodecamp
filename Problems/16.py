n = 6
i=0
l=[]
t=6
while True:
    if t == 0 :
        break
    if t<= 2**i:
        i -=1
        while(i!=-1):
            if t>=2**i:
                l.append(1)
            else:
                l.append(0)
            i -= 1

    i += 1

print(l)