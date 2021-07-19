import  matplotlib.pyplot as plt
import pandas as pd
from sphinx.addnodes import index

data=pd.read_csv("data.csv")

print(data)
query = data[(data["Player"] == "B")]
print(query)
print("Index=",query.index[0])
index=query.index[0]
data.loc[index,["Player"]]="Popat"
print(data)
#print(query)
#print(query.index[0])
data=data.drop([0])
print(data)


"""
#print(data)
#print(type(data))
player=data["Player"]
print(player)
print(type(player))
l=["Player","Run"]
player=data[l]
print(player)
print(type(player))
data["newcol"]="New Data"
print(data)
data["newcol"]=data["Run"]**2
data.to_csv("newdata.csv",index=False)
print(data)
del data["newcol"]
data.append(["M",1,2,3])
print(data)
#query=data[(data["Player"]=="A")]
#print(query)
#print(type(query))
#plt.plot(query["Run"],query["Run"])
#plt.show()
"""