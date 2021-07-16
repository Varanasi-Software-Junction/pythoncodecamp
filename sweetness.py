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
sweetness=[0,2,3,7,3,2,2]
sweetnesscopy=sweetness.copy()
sweetnesscopy.sort()
bitterness=[0,5,4,1,4,9,3]
chocolate=['0','a','b','c','d','e','f']
query=[0,3,5,1,2,6,4]
querycopy=query.copy()
querycopy.sort()
#print(querycopy)
n=len(querycopy)
for i in range(1,n):
    x=querycopy[i]
    queryindex=find(query,x)
    #print(x,queryindex)
    sweetvalue=sweetnesscopy[len(sweetnesscopy)-1]
    sweetnessindex=findAll(sweetness,sweetvalue)
    del sweetnesscopy[len(sweetnesscopy)-1]
    print(sweetvalue,sweetnessindex)
    if len(sweetnessindex)==1:
        output= output + [chocolate[sweetnessindex[0]]]
    else:

print(output)