s="this this is a a cat cat cat ram ram jai it"
l=[]
count=[]
i=0
#j=0
str=""
for i in s:
    #print(i,end="")
    if i==" ":
        if str in l:
            for j in range(len(l)):
                if str == l[j]:
                    count[j] += 1
                    str=""
                    continue

        else:
            l.append(str)
            count.append(1)
            str=""
        continue
    str=str+i

print(l)
print(count)