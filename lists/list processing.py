"""
Lists are created in 2 ways.
1. l=[] Empty list, l=[1,2,3] list with elements

"""
l = []
print(l)
print(type(l))
l = [1, 2, 3]
print(l)
l = list()
print(l)
l = list([1, 2, 3])
print(l)
# The len function gives the length
print("Length is ", len(l))
"""
List is an ordered collection. and indexing starts at 0
"""
print("0: ", l[0], " 1: ", l[1], " 2: ", l[2])
"""
We can also use negative indexing where the last index is -1, then -2,-3 and so on
"""
print("-1: ", l[-1], " -2: ", l[-2], " -3: ", l[-3])
n = len(l)
"""
0=-n
1=-n+1
2=-n+2

Changing from forward to backward is i to -n + i or i-n
"""
for i in range(n):
    print(l[i], " = ", l[-n + i])
# Lists can contain elements of different types
l = [1, "Two", 3, "Four"]
print(l)
#Loop through using in
for x in l:
    print(x)
"""
Looping via index is done using the range 
"""
n=len(l)
for i in range(n):
    print(l[i])

"""
Slicing
General Syntax is 
l[startindex:lastindex + 1]
Extends to the end if not given
"""
l=[0,"One",2,"Three",4,"Five"]
print("1 to 3",l[1:4])
print("1 to end",l[1:])
print("Beginning to 3",l[:4])
print("Complete Array ",l[:])
"""
Negative indexing
"""
print("Last 2 elements",l[-2:])
print(l)
print("2 from last to 4 from last",l[-4:-1])
#General Syntax
print("2 from last to 4 from last",l[-4:-2 + 1])
"""
Functions min and max sorting etc are only supported for elements of the same type
"""
l=[0,1,2,3,4,5]
print("Min ", min(l))
print("Max ", max(l))


