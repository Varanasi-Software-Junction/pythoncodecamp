"""
1. Python Sets are data structures that store data and remove duplicates automatically
2. Sets are made by using the set constructor or a set of curly braces {}.
3. Sets are mutable. This means that elements can be added or removed. Set elements are immutable
means they cannot be changed
4. Sets are unordered. This means there is nothing like s[0],s[1] etc


"""
"""
Create a set
"""
s1 = set([1, 2, 3, 4])
s2 = {1, 2, 3, 4}
print(s1, s2)
print(type(s1), type(s2))  # Types of the objects
# Add elements
s1.add(5)  # Add 1  element
print(s1)
s1.update([1, 2, 3, 4, 5, 6, 7, 8])  # Add multiple elements. Duplicates will be rejected
print(s1)
s1.remove(4)  # Remove elements from the set. Raises a KeyError if it doesn't exist
print(s1)
# s1.remove(4)#This will raise an error
s1.discard(5)  # Discard removes an element but doesn't raise an error if it doesn't exist
print(s1)
s1.discard(5)  # no error
poppedelement = s1.pop()  # Removes a random element and returns it
print(s1, poppedelement)
s1.clear()  # Removes all elements
print(s1)
# Set operations
cricketers = {"A", "C"}
footballers = {"B", "C"}
# Union
u = cricketers.union(footballers)  # All elements with duplicates only once
print("Union ", u)
u = cricketers.copy()  # Make a copy
u.update(footballers)
print("Union ", u)
i = cricketers.intersection(footballers)  # Common elements only
print("Intersection ", i)
i = cricketers.copy()
i &= footballers
print("Intersection ", i)
diff = cricketers.difference(footballers)  # Elements in cricketers but not in footballers
print("Difference ", diff)
diff = cricketers - footballers  # Same as above
print("Difference ", diff)
symmdiff = cricketers.symmetric_difference(footballers)  # Remove common elements
print("Symmetric Difference", symmdiff)
symmdiff = cricketers.copy()
symmdiff ^= footballers
print("Symmetric Difference", symmdiff)
# is subset
a = {1, 2, 3}
b = {1, 2}
print("Subset ", a.issubset(b))
print("Subset ", a <= b)
print("Subset ", b.issubset(a))
print("Subset ", b <= a)
# issuperset
print("Superset ", a.issuperset(b))
print("Superset ", a >= b)
print("Superset ", b.issuperset(a))
print("Superset ", b >= a)
# Disjoint
a = {1, 2}
b = {2, 3}
c = {3, 4}
print("disjoint ", a.isdisjoint(b))
print("disjoint ", a.isdisjoint(c))
# Update methods
a = {1, 2}
b = {2, 3}
c = {3, 4}
d=a.copy()
d.intersection_update(b)
print("Intersection update ",d)
d=a.copy()
d.difference_update(b)
print("Difference update ",d)
d=a.copy()
d.symmetric_difference_update(b)
print("Symmetric difference update ",d)
