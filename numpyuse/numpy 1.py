# Introduction to Numpy
import numpy as np

print(np.__version__)
a = np.array([1, 2, 3, 4, 5])

print("An array ", a)
arr = np.zeros(10)  # Create an array filled with 0s
print("Array of zeroes ", arr)
arr = np.ones(10)  # create an array with 1s
print("Array of ones ", arr)
arr = np.random.randint(9, size=10)  # Create an array of random numbers
print("Array of random elements ", arr)
arr = arr.reshape([2, 5])
print("Array reshaped 2X5\n", arr)
arr = arr.reshape([-1])
print("Array reshaped to one dimension ", arr)
a = np.array([[1, 2], [3, 41]])
print("Element at 0,0 ", a[0, 0])
print("Size of array ", a.size)
print("Shape of array", a.shape)
print("Dimensions of Array", a.ndim)
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
result = np.where(a % 2 == 1)
print("Searching in array ", result)
print(result[0])
for pos in result:
    print("pos", pos, "value", a[pos])
print("Sort", np.sort(a))
print("Reverse", np.flip(np.sort(a)))
