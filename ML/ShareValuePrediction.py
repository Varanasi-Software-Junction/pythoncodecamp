import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
def predictIorD(data,month,year):
    date = data[["Month", "Year"]]
    iord = data["Change1"]
    dtree = DecisionTreeClassifier().fit(date, iord)
    return dtree.predict([[month,year]])
def predictOpen(data,month,year):
    data["Monthno"]=data["Year"]*12 + data["Month"]
    print(data)
    print(year*12+month)
    query=data[(data["Year"]>2015)]
    pf1 = np.polyfit(query["Monthno"],query["Open"],1)
    model1 = np.poly1d(pf1)
    pf2 = np.polyfit(query["Monthno"], query["Price"], 1)
    model2 = np.poly1d(pf2)
    pf3 = np.polyfit(query["Monthno"], query["High"], 1)
    model3 = np.poly1d(pf3)
    pf4 = np.polyfit(query["Monthno"], query["Low"], 1)
    model4 = np.poly1d(pf4)
    plt.plot(query["Monthno"],query["Open"],label="Opening")
    plt.plot(query["Monthno"], model1(query["Monthno"]), label="Predicted Opening")
    plt.legend()
    plt.show()
    plt.plot(query["Monthno"],query["Price"],label="Closing")
    plt.plot(query["Monthno"], model2(query["Monthno"]), label="Predicted Closing")
    plt.legend()
    plt.show()
    plt.plot(query["Monthno"],query["High"],label="Highest in the Month")
    plt.plot(query["Monthno"], model3(query["Monthno"]), label=" Predict Highest in the Month")
    plt.legend()
    plt.show()
    plt.plot(query["Monthno"],query["Low"],label="Lowest in the Month")
    plt.plot(query["Monthno"], model4(query["Monthno"]), label=" PredictLowest in the Month")
    plt.legend()
    plt.show()
    #print(model(year*12+month))
    return model1(year*12+month),model2(year*12+month),model3(year*12+month),model4(year*12+month)
data = pd.read_csv("sharesData.csv")
print(data)
date = data[["Month","Year"]]
iord = data["Change1"]
print(date)
# predicting whether the stock price will increase or decrease
dtree = DecisionTreeClassifier().fit(date,iord)
print(dtree.predict([[8,2021],[9,2021]]))
print("[1] means share Value will Increase this month")
print("[0] means share value will decrease this month")
print(predictIorD(data,10,2022))
# predicting opening price of stock every month
print(predictOpen(data,12,2030))