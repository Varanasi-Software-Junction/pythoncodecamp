import numpy as np#polyfit, poly1d, linspace
from sklearn.metrics import r2_score #r2_score to find coefficient of corelation
from sympy import diff,symbols # used in process of differentiation
ix=[1,2,3,4,5]
iy=[2,5,10,17,26]
#curvefitting
pf = np.polyfit(ix,iy,2)# 1 is for degree of equation of curve for curve fitting
print(pf)# gives coefficient of equation e.g. x^2 +3x+1 then it will give [1. 3. 1.]
print(type(pf))
model = np.poly1d(pf)   # it gives model
print(model)
print(type(model))
#predicting value
px = [7,8,9,10]
py = model(px)           # prediction
print(py)                # printing prediction
#coefficient of correlation
coeff=r2_score(iy,model(ix))
print("Coefficient of Correlation=",coeff)
#Differentiation
a= symbols('x') # if two variable equation then a,b = symbols('x,y')
gradient = diff(model(a),a)
print(gradient)
 #OR
gradient1 = model.deriv()
print(gradient1)





