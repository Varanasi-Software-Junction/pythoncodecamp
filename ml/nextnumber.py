n=22351
l=[]
s=str(n)
for ch in s:
    l= l + [int(ch)]
highest=sorted (l,reverse=True)
s=""
for ch in highest:
    s=s+ str(ch)
highest=int(s)
n=9

for i in range(n +1,highest+1):
    print(i)
