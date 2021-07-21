class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.address=address
        self.age=age
    def __str__(self):
        return "Name={0}, Age = {1}, Address={2}".format(self.name,self.age,self.address)

p=Person("Pappu",50,"Delhi")
print(p)
 