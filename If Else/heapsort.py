def makeHeap(a):
    n=len(a)
    heap=[0 for i in range(n+1)]
    for i in range(n):
        value=a[i]
        pos=i+1
        heap[pos]=value
        while True:
            parentpos=pos//2
            if parentpos<=0:
                break
            if heap[parentpos]>=value:
                break
            heap[pos],heap[parentpos]=heap[parentpos],heap[pos]
            pos=parentpos
    return heap
    
def heapSort(a):
    heap=makeHeap(a)
    heaplength=len(heap)
    n=len(a)
    for i in range(1,heaplength):
        value=heap[1]
        a[n-i]=value
        pos=1
        heap[1]=heap[heaplength-i]
        value=heap[1]
        heapsize=heaplength-1-i
        while True:
            left=2*pos
            right=left+1
            if left>heapsize:
                break
            max=heap[left]
            maxpos=left
            if right<=heapsize:
                if heap[right]>max:
                    max=heap[right]
                    maxpos=right
            if value>=max:
                break
            heap[pos],heap[maxpos]=heap[maxpos],heap[pos]
            pos=maxpos
            value=max


    return a
a=[5,3,8,1,80,9]
print(a)
a=heapSort(a)
print(a)
