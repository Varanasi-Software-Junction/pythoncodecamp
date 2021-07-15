import pandas as pd
data=pd.read_csv("data.csv")
print(data)
print(data[(data["Run"]<=5000) |  (! (data["Run"]<=5000))])