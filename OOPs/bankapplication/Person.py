class Person:
    def __init__(self, name=None, age=None, address=None):
        if name is not None:
            self.name = name
        else:
            self.name = input("Enter name\n")
        if address is not None:
            self.address = address
        else:
            self.address = input("Enter address\n")
        if age is not None:
            self.age = age
        else:
            self.age = int(input("Enter age\n"))

    def __str__(self) -> str:
        return "Name={0}, Age={1}, Address={2}".format(self.name, self.age, self.address)


