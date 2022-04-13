import Person as pp


class Employee(pp.Person):
    def __init__(self, name, age, address, salary, post):
        super().__init__(self, name, age, address)
        self.salary = salary
        self.post = post
        # pp.Person.__init__(self,name,age,address)

    def __str__(self):
        return "{0}, Salary={1}, Post={2}".format(pp.Person, self.salary,self.post)


e = Employee("pappu", 56, "Delhi", 1000, "VP")
print(e)
