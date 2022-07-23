def heapSort(heap):
    n = len(heap)
    a = [0] * (n-1)
    for i in range(1, n):
        a[n -1- i] = heap[1]
        length = n - i + 1
        heap[1] = heap[n - i]
        length -= 1
        pos = 1
        while True:
            left = 2 * pos
            right = left + 1
            if left > length:
                break
            if right > length:
                if heap[pos] >= heap[left]:
                    break
                heap[pos], heap[left] = heap[left], heap[pos]
                break
            if heap[right] > heap[left]:
                maxpos = right
            else:
                maxpos = left
            if heap[pos] >= heap[maxpos]:
                break
            heap[pos], heap[maxpos] = heap[maxpos], heap[pos]
            pos = maxpos
    return a


def makeHeap(a):
    n = len(a)
    heap = [0] * (n + 1)
    for i in range(n):
        heap[i + 1] = a[i]
        pos = i + 1
        while True:
            parent = pos // 2
            if parent < 1:
                break
            if heap[parent] >= heap[pos]:
                break
            heap[pos], heap[parent] = heap[parent], heap[pos]
            pos = parent
    return heap


a = [1, 2, 33, 4, 5, -6, 7]
print(a)
heap = makeHeap(a)
print(heap)
a = heapSort(heap)
print(a)
