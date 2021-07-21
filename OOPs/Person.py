import book as book
class Person:
    def __init__(self,name,age,address,book):
        self.name=name
        self.address=address
        self.age=age
        self.book=book
    def __str__(self):
        return "Name={0}, Age = {1}, Address={2}, Book={3}".format(self.name,self.age,self.address,self.book)
b1=book.Book("Basic C",100,"Cb")
p=Person("Pappu",50,"Delhi",b1)
print(p)
