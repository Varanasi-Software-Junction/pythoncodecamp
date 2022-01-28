a=[22,34,211,54,67,87,65,36,95,16,5,18]
lar=a[0]
sm=a[0]
for element in a:
    if(element>lar):
        lar=element
    elif(element<sm):
        sm=element
print("Max element= ",lar)
print("Min element= ",sm)