class Book:
    def __init__(self,bookname,price,subject):#Constructor
        self.bookname=bookname
        self.price=price
        self.subject=subject
    def __str__(self):#toString
        return "Bookname = {0}, Price = {1}, Subject = {2}".format(self.bookname,self.price,self.subject)

b1=Book("Basic C",100,"Cb")
b2=Book("Adv C",100,"C")
print(b1)
print(b2)
print("Book = {0}".format(b1))
