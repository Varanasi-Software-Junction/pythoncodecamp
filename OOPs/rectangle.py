class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        return 2* self.length + 2* self.breadth
    def area(self):
        return self.length * self.breadth
    def __str__(self):
        return "Length = {0}, Breadth={1}, area = {2}".format(self.length,self.breadth,self.area())
class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)

r1=Rectangle(4,3)
print(r1.area())
print(r1)
s1=Square(2)
print(s1)
print(s1.perimeter())