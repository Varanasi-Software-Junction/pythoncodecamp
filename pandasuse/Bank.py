import pandas as pd
def checkacc(data, acc): #It will take dataframe and acc as input and give whether account no. exist or not
    t = False
    if acc in list(data['Accno']):
        t = True
    return t
def find(data, a): # It will take dataframe and account as input and givethe records of account no. a
    query= data[(data['Accno'] == a)]
    return query

def checkbal(data, acc): # It will take dataframe and accno and  give Balance of given account no
    if not checkacc(data,acc):
        return "!!Wrong Account no.!!"
    query=find(data,acc)
    index=query.index[0]
    return query.loc[index,['Balance']][0]



def deposit(data): # It will take dataframe as input data and deposit the money
    accno = int(input('Enter your account no. :'))
    if not checkacc(data, accno):
        print("!!!Invalid Account Number!!!")
        return

    query = find(data, accno)
    dep = int(input('Enter amount :'))

    #reqindex = data.index[data['Accno'] == accno]
    reqindex = query.index[0]
    #print(reqindex)
    data.loc[ reqindex,['Balance']] += dep
    print(dep,' $ Deposited in your account')

def withdraw(data): # It will withdraw money from given account no.
    accno=int(input('Enter your acount number :'))
    if not checkacc(data, accno):
        print("!!!Invalid Account Number!!!")
        return data
    amount = int(input("Enter amount :"))
    query = find(data, accno)
    index = query.index[0]
    print(type(query))
    print(query.loc[index,['Balance']][0])
    if query.loc[index,['Balance']][0] < amount:
        print("Withdraw Failed \n Not enough Balance")
        print('Your Balance is only ', query.loc[0,['Balance']][0],)
        return


    data.loc[index , ['Balance']] -= amount
    print('Withdraw Successful')
    #print(data)

def openacc(data): # It will open new account
    accno = int(input("Enter the new account no :"))
    if checkacc(data , accno):
        print('Account Number Already Exist')
        return
    name = input('Enter your name :')
    balance = int(input('Enter your account opening balance :'))
    newrow ={'Accno':accno,"Name":name,"Balance":balance,"Status":'Open'}
    data = data.append(newrow, ignore_index=True)
    print('Account Opened successfully')
    return data

def closeacc(data): # It will open new account
    accno=int(input('Enter the account no :'))
    query = find(data,accno)
    i = query.index[0]
    data.loc[i,['Status']]='Closed'
    print('Account Closed')

data=pd.read_csv('E:\pythoncodecamp\data\Bank.csv')
""" record={"Accno":3,"Name":"Shivank","Balance":30000}

data = data.append(record, ignore_index=True) # inserting a row in dataframe
"""

while(True):
    n=int(input(' 0.Exit\n 1.Open new account\n 2.Check Balance \n 3. Deposit\n 4. Withdraw\n 5.Close Account \n Type Option : '))
    if n == 0 :
        data.to_csv('E:\pythoncodecamp\data\Bank.csv', index=False)
        break
    elif n == 1 :
        data = openacc(data)
    elif n == 2 :
        accno=int(input("Enter your account no. :"))
        amount = checkbal(data,accno)
        print(amount,"Rupees")
    elif n == 3:
        deposit(data)
    elif n == 4:
        withdraw(data)
    elif n == 5:
        closeacc(data)
    else:
        print("!!You Entered the wrong key!!")
    input("Press Enter to continue ")


#data=data.drop(3)  #for deleting row with index 3








