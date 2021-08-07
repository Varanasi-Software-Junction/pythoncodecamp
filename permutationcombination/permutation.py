def permute(index,maxindex,l):
        for  i in range(maxindex+1):
            if i in l[: index]:
                continue
            l[index] = i
            if index == maxindex:
              print(l)
            else:
                permute(index + 1,maxindex,l)
n=3

l=list(range(n))
permute(0,n-1,l)