import Person1 as pp
class Employee(pp.Person):
    def __init__(self,name,age,address,salary,post):
        pp.Person.__init__(self,name,age,address)
        self.salary = salary
        self.post = post

    def __str__(self):
        return"Name = {0} , Age = {1}, Address = {2}, salary = {3} , post ={4}".format(self.name,self.age,self.address,self.salary,self.post)

class Manager(pp.Person):
    '''def __init__(self):
    def abhi(self):
        print(self.name)'''


    #e1 = Employee('Abhishek',21,'Varanasi',1000000000,'VP')
#print(e1)
m = Manager('Manas',22,'Varanasi')
print(m)
