l = [2,5,9,1,4,5,3,4,6,8,0,1]
n = len(l)
l= l + [l[n-1]-1]
n= n + 1
increasingsequences = []
currentseq = [l[0]]
for i in range(1,n):
    prev = l[i-1]
    current = l[i]
    if current >= prev:
        currentseq = currentseq + [current]
    else:
        increasingsequences = increasingsequences + [currentseq.copy()]
        currentseq.clear()
        currentseq=[current]
print(increasingsequences)

