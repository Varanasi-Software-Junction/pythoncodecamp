l = [2,5,9,1,6,8,4,1]
s = 10
l.sort()
print(l)
b=[]
print(l)
for i in range(len(l)):
    print("for i {}".format(i))
    sum = l[i]
    b.append(i)
    j = i+1
    while j<len(l) and sum < s :
        print("while j ",j)
        sum += l[j]
        print(sum)
        b.append(j)
        j += 1
    print(sum)
    if sum == s:
        print("got it")
        for i in range(len(b)):
            print(l[b[i]])
    b.clear()