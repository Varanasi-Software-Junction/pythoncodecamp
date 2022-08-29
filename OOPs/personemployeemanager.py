"""
Imagine the following scenario.

1. You developed a class called Person with the following data to be used in
an address book application. We store name, address and mobile numbers in the Person class

2. The nextchar project we are asked to manage Employee details so we plan an Employee class
The Employee class needs to store name, address, mobileno, post and salary.

The first 3 members are common to both classes. More importantly every Employee is a Person.

This is the exact situation in which inheritance is done.





"""


class Person:
    def __init__(self, name, address, mobile):
        self.name = name
        self.address = address
        self.mobile = mobile

    def __str__(self):
        return "Name={0}, Address={1}, Mobile={2}".format(self.name, self.address, self.mobile)


class Employee(Person):  # Extended from Person
    def __init__(self, name, address, mobile, post, salary):  # Constructor
        super(Employee, self).__init__(name, address, mobile)  # Super class constructor
        self.post = post
        self.salary = salary

    def __str__(self):
        return "{0}, Post = {1}, Salary={2}".format(super().__str__(), self.post, self.salary)


p = Person("Sachin", "Mumbai", "9987887654")
print(p)
e = Employee("Sachin", "Mumbai", "9876543212", 'Batsman', 1000)
print(e)
