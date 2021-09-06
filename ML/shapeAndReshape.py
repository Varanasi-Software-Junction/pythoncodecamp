import numpy as np
from sklearn.metrics import r2_score
x = [1,2,3,4,5,6,7,8]
x = np.array(x)
x=x/8
print(x)
print(x*2)
print(x*x)
"""
x=np.ones(36)
print(x.shape)
x=x.reshape(2,2,-1)
print(x)
x=x.reshape(-1)
print(x.shape)
#36 1 X 36, 2 X 18, 18 X 2, 2 X 3, 6
"""