n=100
count=1
for i in range(1,n+1):
    for j in range(i+1,n+1):
        for k in range(j+1,n+1):
            if i*i + j*j == k*k:
                print(count,")",i,j,k)
                count+=1