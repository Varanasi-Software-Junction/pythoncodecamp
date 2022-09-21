import matplotlib.pyplot as plt

labels = ["One", "Two", "Three"]
data = [100, 300, 400]
plt.pie(data, labels=labels, autopct="%1.2f%%", explode=[0.1, 0.3, 0.1], colors=["red", "green", "yellow"])
plt.legend()
plt.show()
