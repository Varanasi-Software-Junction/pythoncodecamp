"""
A dictionary is collection of values indexed by keys.
Keys cannot be repeated, values can be repeated
Empty Dictionaries are created by {} brackets or dict()

"""
d = {}
print(d, type(d))
d = dict()
print(d, type(d))
"""
Dictionaries with keys
d={1:"One",2:"Two"}
1 is key and "One" is value
"""
d = {1: "One", 2: "Two"}
print(d)
# Add a key value to dictionary using d[key]=value. Updating is done in the same way
d[3] = "Three"
print(d)
d[3] = "3-Three"  # Replace
print(d)
"""
dictionary has three collections Items, Keys and Values
"""
print("Items")
for key, value in d.items():
    print(key, value)
print("Keys")
for key in d.keys():
    print(key)
print("Values")
for value in d.values():
    print(value)
# Searching for values. get method returns None if value is not found
value = d.get(0)
print(value)  # None because key 0 does not exist
value = d.get(1)
print(value)  # Key exists
# We cn also search by direct indexing but it throws exception if not found
print(d[2])  # Value found
# print(d[9])#raises KeyError because not found
"""
Removing elements
"""
d.pop(2)  # Throws exception if key not found
print(d)
d.popitem()  # Remove the last element
print(d)
