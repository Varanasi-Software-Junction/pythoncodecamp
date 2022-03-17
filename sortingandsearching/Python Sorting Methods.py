a = [16, 0, 1, 9, 70]  # Create a list a
print(a)
a.sort()  # Sort the array
print(a)  # The sorted array
a.sort(reverse=True)  # Sort the array in reverse order
print(a)  # The sorted array
# Python supports sorting of lists of different types
a = ["cat", "dog", "ball", "apple"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
# Using the sorted method. This methods returns a sorted array and leaves the original unchanged
a = ["cat", "dog", "ball", "apple"]
sortedarray = sorted(a)
print("Original Array ", a)
print("Sorted Array ", sortedarray)
reversesortedarray = sorted(a, reverse=True)
print("Reverse Sorted Array ", reversesortedarray)

# Sorting using key. You can use any function that takes exactly one argument  of the given data type
# Let us say we want to sort by length of the words.
a = ["cat", "dog", "ball", "apple"]
a.sort(key=len)
print(a)
a.sort(key=len, reverse=True)
print(a)


# Making our own function
def lastChar(s):
    return s[len(s) - 1]


a.sort(key=lastChar)
print(a)
# Using lambda
a.sort(key=lambda x: x[len(x) - 1], reverse=True)  # Sorting by last character and reverse
print(a)
# Using the cmp function
import functools as ft


def mycompare(a, b):
    # Return -ve if a<b, 0 if a==b and +ve if a>b
    # This will sort in reverse order
    return b - a


a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(mycompare))
print(a)
# The same thing using lambda
a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)
# Generate a random array and sort it
from numpy import random

a = list(random.randint(100, size=(10)))
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)
# Another way of doing the same thing
a = [random.randint(100) for x in range(10)]
a.sort(key=ft.cmp_to_key(lambda a, b: a - b))
print(a)
