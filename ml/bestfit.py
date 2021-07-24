import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
def bestfitModel(x,y):
    bestcoeff=0
    bestmodel=None
    bestpower=0
    for r in range(1,6):
        model = numpy.poly1d(numpy.polyfit(x, y, 2))
        coeff=r2_score(y, model(x))
        if coeff>bestcoeff:
            bestcoeff=coeff
            bestmodel=model
            bestpower=r
    return bestcoeff,bestmodel,bestpower



x = [1,2,3,4]

listy=[[1,2,3,4],[1,4,9,16],[1,8,27,64],[1,16,81,256]]
y=listy[3]#Change Here 0,1,2,3
plotx=[-2,-1,0,1,2,3,4,5,6,7,8]
coeff,model,power=bestfitModel(x,y)
print("Coeff",coeff,"Power",power,"Model",model)
plt.scatter(x,y,color="yellow")
plt.plot(x,y,"b-",label="Original",linewidth=4)
plt.plot(plotx, model(plotx),"r-",label="Predicted",alpha=0.5,linewidth=4)
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.show()
xvalue=7
predict=model(xvalue)
print("Predicted",predict)