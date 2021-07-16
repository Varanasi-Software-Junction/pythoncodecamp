def findAll(lst,value):
    l=[]
    n = len(lst)
    for i in range(1, n):
        if value == lst[i]:
            l=l + [i]
    return  l
def find(lst,value):
    n=len(lst)
    for i in range(1,n):
        if value==lst[i]:
            return i
    return -1
output=[]
sweetness=[2,3,7,3,2,2]
bitterness=[5,4,1,4,9,3]
chocolate=['a','b','c','d','e','f']
query=[3,5,1,2,6,4]
print(sweetness)
print(bitterness)
print(chocolate)
print(query)
n=len(sweetness)
for i in range(n-1):

    pos=i
    for j in range(i+1,n):
        if sweetness[j]<sweetness[pos]:

            pos=j
        elif sweetness[j]==sweetness[pos]:
            if bitterness[j]>bitterness[pos]:
                minbitterness=bitterness[j]
                pos=j
            elif bitterness[j]==bitterness[pos]:
                if chocolate[j]>chocolate[pos]:
                    pos=j


    t=sweetness[i]
    sweetness[i]=sweetness[pos]
    sweetness[pos]=t
    t=bitterness[i]
    bitterness[i]=bitterness[pos]
    bitterness[pos]=t
    t=chocolate[i]
    chocolate[i]=chocolate[pos]
    chocolate[pos]=t
print()
print(sweetness)
print(bitterness)
print(chocolate)

