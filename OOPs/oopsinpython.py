



"""
Computer Programming started with what is called Procedural Programming
Characteristics of Procedural Programming
1. A set of global variables that were accessible throughout the program.
2. different functions to do specific tasks. Functions could have their parameters and
local variables.
It was difficult to make programs that were complex and that went up to around 1000 lines
Imagine a situation where a laptop is not divided into components like
hard disk, mouse pad, screen etc but is  simple circuit
The problems
1. Too complex logic
2. Finding faults was difficult, isolating faults was difficult
3. No part evolution or replacement. If the screen goes bad you replace it. No part enhancement.
You need higher capacity hard disk then simply replace the part

Computer programmers decided that component based systems must come into software development.
This is called Object Oriented Programming or OOPS

Basic terminology
Imagine a situation where your company decides to make a car.
What are the steps that you follow?
1. Decide upon the final car. The design and facilities
2. Break the car into parts and decide their functionality. Things like wheels, horns,
steering, brakes etc
3. Break the parts into smaller-simpler parts and carry on till you come to  situation
where things can be implemented
4. Make the parts and combine.
This is top down design. We started with the final car and broke it into parts.

For the nextchar car we will already have a stock of parts. We will try and use this to the
maximum. Bottom-up design

Terms
Class - the design of an object. In the case of a Car a list of parts with functions
Generally called blueprint
Object- Instance of a class. The actual produced car. Once a class is made we can create
unlimited objects.
Encapsulation-- Putting multiple objects  inside a new object and leaving only the interfaces out
is called encapsulation.

Interface -- Points where process communicate. Eg keyboard, mouse, screen in a laptop.
steering, horn etc in a car

Abstraction -- Abstraction is learning how to use an object without knowing its implementation
details. The driver shouldn't need to learn how a car is made to actually drive.
Implementation details must be hidden. This also promotes Device Independence.

Polymorphism --- The same command meaning different things based on the context, the number
of inputs and the types of inputs. For example if you are holding a bat and someone says hit
hard you understand he is talking about hitting the ball. If you are holding a badminton racket it
means something else
The + command used with strings concatenates but used with numbers it adds numerically.
"1" = "2" = "12" while 1 + 2 = 3

Inheritance-- Developing a new version of a product maintaining backward compatibility.

Class variables --- variables accessible throughout the object
Constructor --- Adding the parts to the body. In Python its the __init__ function
toString --- Gives a string output of the current object.




"""


class Car:  # Starting the Car class
    def __init__(self, carmodel, carprice, carcompany):  # Constructor. Self is a reference to the current object
        self.carmodel = carmodel  # Transferring to the current object
        self.carprice = carprice
        self.carcompany = carcompany

    def __str__(self):  # String representation of the class
        return "Model={0}, Company = {1}, Price = {2}".format(self.carmodel, self.carcompany, self.carprice)


c1 = Car("800", 100000, "Maruti")
print(c1)
c2 = Car("Esteem", 1000000, "Maruti")
print(c2)




