a=[45,34,65,87,90,1,4,5,6,8]
even=[]
odd=[]
for element in a:
    if element % 2 == 0:
        even.append(element)
    else:
        odd.append(element)
print("Even to Odd: ",even+odd)
