from numpy.polynomial import polynomial as poly
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np
import random
import math
actualx =[1,2,3,4]#
actualy=[3*x+1 for x in actualx]
#Linear Inputactualy=[4, 7, 10, 13]
equation=poly.Polynomial.fit(actualx,actualy,deg=deg).convert()
# Equation based on the input dataprint("Equation=",equation)
#Print the generated equationprint(actualx)print(actualy)predictionx=np.linspace(1,10,10)# values from 1 to 10. Predicted values input

#Quadratic 