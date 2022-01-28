a=[34,22,45,32,78,43,12,3,98]
sm=a[0]
lr=a[0]
for i in a:
    if(i<sm):
        sm=i
    elif(i>lr):
        lr=i
print(a)
print("dif between ",lr," and " , sm, " is : ",lr-sm)