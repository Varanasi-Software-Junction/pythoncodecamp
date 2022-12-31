import pickle

print("Hello")


class Book:
    def __init__(self, bookname, subject, price):
        self.bookname = bookname
        self.subject = subject
        self.price = price

    def __str__(self):
        return "Book Name={0}, Subject={1}, Price={2}".format(self.bookname, self.subject, self.price)


data = {}
data[1] = Book("Basic C", "C", 100)
data[2] = Book("Basic C++", "C++", 200)

datafile = open('datastore', 'ab')
pickle.dump(data, datafile)
datafile.close()
datafile = open('datastore', 'rb')
data = pickle.load(datafile)
print(data)
for key, value in data.items():
    print(key, ':', value)
datafile.close()
