import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
def bestfitModel(x,y):
    bestcoeff = 0
    bestmodel = None
    bestpower = 0
    for r in range(1,6): # loop for checking which type of curve fits best on give data
        pf = numpy.polyfit(x,y,r) #numpy.polyfit(x,y,r) x and y are varaibles r is degree of function in which we want to regret
        model = numpy.poly1d(pf) # gives us equation after regression
        coeff = r2_score(y,model(x)) # coefff is coeff of correlation
        if coeff > bestcoeff:
            bestcoeff = coeff
            bestmodel = model
            bestpower = r
    return bestcoeff, bestmodel,bestpower

x=[1,2,3,4]
listy = [[1,2,3,4],[1,4,9,16],[1,8,27,64],[1,16,81,256]]
y=listy[3] #Change Here 0,1,2,3
plotx=[-2,-1,0,1,2,3,4] # for preditcting
coeff,model,power = bestfitModel(x,y)
print("Coeff",coeff,"Power",power,"\n model\n",model)
print()
plt.scatter(x,y,color="red")
plt.plot(plotx,model(plotx),color="red",label="Prediction",alpha=0.5,linewidth=4)
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.show()
print(numpy.derive(model))
