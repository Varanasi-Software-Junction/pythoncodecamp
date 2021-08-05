n=22351
l=[]
s=str(n)
for ch in s:
    l= l + [int(ch)]
n = len(l)

print(l)
dobreak = False
for i in reversed(range(1,n)):
    num1 = l[i]
    for j in reversed( range(0,i)):
        num2=l[j]
        if num1>num2:
            dobreak = True
            t = l[j]
            l[j] = l[i]
            l[i] = t
            prevpart = l[:j+1]
            nextpart = l[j+1:]
            nextpart.sort()
            l = prevpart + nextpart
            break
    if dobreak:
        break
if not dobreak:
    print("ALready largest")
else:
    print(l)




