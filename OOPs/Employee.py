import Person as pp
class Employee(pp.Person):
    def __init__(self, name,age,address,salary,post):
        pp.Person.__init__(self,name,age,address)
    def __str__(self):
        return "{0}, Salary={1}, Post={2}".format(pp.Person,self.s)
e=Employee("pappu",56,"Delhi",1000,"VP")