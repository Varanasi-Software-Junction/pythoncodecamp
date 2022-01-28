a = [1,2,1]
noofparts = 2
n = len(a)
partsize = int(n / noofparts + 0.5)
print(noofparts, n, partsize)
divisions = [0 for x in range(noofparts)]
#print(divisions)
i = 0
pos = 0
while i < noofparts:
    divisions[i] = a[pos:pos + partsize]
    i += 1
    pos += partsize
#print(divisions)
divisionsum=[0]*noofparts
maxm = sum(divisions[0])
maxpos = 0
for i in range(noofparts):
    item = divisions[i]
    divisionsum[i]=sum(item)
    if sum(item) > maxm:
        maxm = sum(item)
        maxpos = i
    print(item, "=", sum(item))
print(maxm, maxpos)
min_load=maxm
prevmax=maxm
print("*******")
while True:
    print("*******")
    print(prevmax,maxm,maxpos)
    print(divisions)
    print(divisionsum)
    prevmax = maxm
    if maxpos==0:
        #divisions[maxpos]
        rem=divisions[maxpos].pop(-1)

        divisions[maxpos+1].insert(0,rem)
        divisionsum[maxpos]=divisionsum[maxpos]-rem
        divisionsum[maxpos+1]=divisionsum[maxpos+1]+rem
        maxm = max(divisionsum[maxpos], divisionsum[maxpos + 1])
        if divisionsum[maxpos + 1] > divisionsum[maxpos]:
            maxpos += 1

    elif maxpos==noofparts-1:
        rem = divisions[maxpos].pop(0)
        divisions[maxpos - 1].append(rem)
        divisionsum[maxpos] = divisionsum[maxpos] - rem
        divisionsum[maxpos - 1] = divisionsum[maxpos - 1] + rem
        maxm = max(divisionsum[maxpos - 1], divisionsum[maxpos])
        if divisionsum[maxpos - 1] > divisionsum[maxpos]:
            maxpos -= 1

    else:
        remleft=divisions[maxpos][0]
        remright=divisions[maxpos][-1]
        print(divisions)
        print("sum1")
        sum1=max(divisionsum[maxpos-1]+remleft,divisionsum[maxpos]-remleft)
        sum2=max(divisionsum[maxpos]-remright,divisionsum[maxpos]+remright)
        if sum1<sum2:
            rem=divisions[maxpos].pop(0)
            divisions[maxpos-1].append(rem)
            divisionsum[maxpos-1]+=rem
            divisionsum[maxpos]-=rem
            maxm=sum1
            if divisionsum[maxpos-1]>divisionsum[maxpos]:
                maxpos-=1
        else:
            rem=divisions[maxpos].pop(-1)
            divisions[maxpos+1].insert(0,rem)
            divisionsum[maxpos + 1] += rem
            divisionsum[maxpos] -= rem
            maxm=sum2
            if divisionsum[maxpos+1]>divisionsum[maxpos]:
                maxpos+=1
    if maxm<min_load:
        min_load=maxm
    if maxm==prevmax or prevmax < maxm:
        break
print(min_load)








