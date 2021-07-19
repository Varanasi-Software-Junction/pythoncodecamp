import pandas as pd
data=pd.read_csv('E:\pythoncodecamp\data\Bank.csv')
""" record={"Accno":3,"Name":"Shivank","Balance":30000}

data = data.append(record, ignore_index=True) # inserting a row in dataframe
"""


def deposit(data):
    accno=int(input('Enter your account no. :'))
   # query=data[data['Accno'] == accno]
    dep = int(input('Enter amount :'))
    condition=data['Accno'] == accno
    reqindex = data.index[condition]
    print(reqindex[0])
    data.loc[ reqindex[0] ,['Balance']] += dep
    print(data)
   # print(data)
    #print(data.loc[])


#d={0:"break", 1:"deposit",2:"withdraw",3:"openacc",4:"closeacc"}
#print(data)
deposit(data)






