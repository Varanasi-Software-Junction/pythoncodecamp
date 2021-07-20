class Rectangle:
    def __init__(self, l,b): # constructor
        self.b = b
        self.l = l
    def __str__(self): # called whenever object is printed
        return "Rectangle having length = {0}  and breadth = {1}".format(self.l,self.b)
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b


r1 = Rectangle(4,5)
print(r1)
print("Area of rectanle =",r1.area())
print("Perimeter of rectangle = ",  r1.perimeter())