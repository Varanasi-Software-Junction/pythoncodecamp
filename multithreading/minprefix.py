a=["aa","aaaa","aaa","ageek"]
a.sort()
print(a)
first=a[0]
last=a[len(a)-1]
n=len(first)
prefix=""
match=True
i=0
while i<=n-1 and  match:
    print('Here')
    prefix=prefix + first[i]
    match=last.startswith(prefix)
    i+=1
print(prefix)
