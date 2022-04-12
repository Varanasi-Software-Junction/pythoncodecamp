"""
Starting OOPs in Python.
The topics we will cover are.
1. Making Classes
2. Methods inside classes
3. Using classes inside classes
4. Inheritance
5. Multiple inheritance
6. Operator  overloading

"""


class Book:  # Definiton of class begins

    def __init__(self, bookName, price, subject):  # Constructor
        # self is the equivalent of this in Java and CPP. We can use any name for self.
        # def __init__(xyz, bookName, price, subject): is also valid
        self.bookName = bookName  # Copy bookName parameter to the class variable
        self.price = price
        self.subject = subject

    def __str__(self):  # toString. WIll be used if class object is printed
        return "Bookname = {0}, Price = {1}, Subject = {2}".format(self.bookName, self.price, self.subject)


b1 = Book("Basic C", 100, "Cb")
b2 = Book("Adv C", 100, "C")
print(b1)
print(b2)
print("Book = {0}".format(b1))
