import random

randomlist = [random.randrange(6) for i in range(10)]
"""
random.randrange(start, stop[, step])
Return a randomly selected element from range(start, stop, step). This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
https://docs.python.org/3.10/library/random.html#random.randrange
"""
print("Input List ", randomlist)
n = len(randomlist)
randomlist.append(randomlist[-1] - 1)
maxlist = []
maxlength = 0;
n += 1
p1 = 0
for i in range(1, n):
    if randomlist[i] < randomlist[i - 1]:
        p2 = i
        if p2 - p1 > maxlength:
            maxlength = p2 - p1
            maxlist = randomlist[p1:p2]
        #print(randomlist[p1:p2])
        p1 = i
        # print(i,i-1)
print("Max sequence ", maxlist)