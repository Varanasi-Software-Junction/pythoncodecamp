import numpy as np   
A = np.array([[2, 3], 
                 [3, 4]])
b = np.array([8, 11])
   
solution = np.linalg.solve(A, b)
print("Solution:", solution)