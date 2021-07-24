list=[3,5,9,1,4,5,3,4,6,8,0,1]
sublist=[3,5,9,1,7]
found =0
for i in range(len(list)):
    k=i
    j=0
    count =0
    while(j<len(sublist) and list[k] == sublist[j] ):
        k +=1
        j +=1
        count +=1
    if count == len(sublist):
        print("starting point of sublist is index {0}".format(i) )
        found =1
        break
if found == 0:
    print(sublist," is not a sublist of ",list)