import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("mov1.csv")
print(data)
f=100000
data["x"]=data["x"]//f
data["y"]=data["y"]//f
print(data)
brange = ["1850-1950","1950-2100","2100-2300","2300-2400","2400-2600","2600-2800","2800-4000"]
budget=2700#change budget here
if budget >= 1850 and budget < 1950:
    d1 = data[(data["x"] >= 1850) & (data["x"] < 1950)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 1850 to 1950")
    plt.show()
elif budget >= 1950 and budget < 2100:
    d1 = data[(data["x"] >= 1950) & (data["x"] < 2100)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 1950 to 2100")
    plt.show()

elif budget >= 2100 and budget < 2300:
    d1 = data[(data["x"] >=2100) & (data["x"] < 2300)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 2100 to 2300")
    plt.show()
elif budget >= 2300 and budget <= 2400:
    d1 = data[(data["x"] >= 2300) & (data["x"] < 2400)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 2300 to 2400")
    plt.show()
elif budget >= 2400 and budget <= 2600:
    d1 = data[(data["x"] >= 2400) & (data["x"] < 2600)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 2400 to 2600")
    plt.show()
elif budget >= 2600 and budget <= 2800:
    d1 = data[(data["x"] >= 2600) & (data["x"] < 2800)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 2600 to 2800")
    plt.show()
elif budget >= 2800 and budget <= 4000:
    d1 = data[(data["x"] >= 2800) & (data["x"] < 4000)]
    print(d1)
    label = ["0-4000", "4000-6000", "6000-8000", "8000-10000", "10000-16000"]
    labelcount = [0, 0, 0, 0, 0]
    for i in d1["y"]:
        if i < 4000:
            labelcount[0] += 1
        elif i < 6000:
            labelcount[1] += 1
        elif i < 8000:
            labelcount[2] += 1
        elif i < 10000:
            labelcount[3] += 1
        elif i < 16000:
            labelcount[4] += 1

    plt.pie(labelcount, labels=label, autopct="%1.2f%%")
    plt.title("Budget = 2800 to 4000")
    plt.show()

