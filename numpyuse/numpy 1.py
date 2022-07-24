# Introduction to Numpy
import numpy as np

print(np.__version__)
a = np.array([1, 2, 3, 4, 5])

print(a)
arr = np.zeros(10)
print(arr)
arr = np.ones(10)
print(arr)
arr = arr.reshape([2, 5, 1, 1])
print(arr)
arr = arr.reshape([-1])
print(arr)
a = np.array([[1, 2], [3, 4]])
print(a[0, 0])
print(a.size)
print(a.shape)
result = np.where(a % 2 == 1)
print(result)
print(result[0])
print(np.flip(np.sort(a)))
