import book as book

'''
Using a class in another class. We have imported the Book class
'''


class Person:
    def __init__(self, name, age, address, mybook):
        self.name = name
        self.address = address
        self.age = age
        self.book = mybook

    def __str__(self):
        return "Name={0}, Age = {1}, Address={2}, Book=({3})".format(self.name, self.age, self.address, self.book)


b1 = book.Book("Basic C", 100, "C")
p = Person("Raju", 50, "Delhi", b1)
# print(p)
