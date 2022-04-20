<<<<<<< HEAD
=======
"""
Overloadable Operators
object.__lt__(self, other) <
object.__le__(self, other) <=
object.__eq__(self, other) ==
object.__ne__(self, other) !=
object.__gt__(self, other) >
object.__ge__(self, other) >=
x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), x!=y calls x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).



object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)


These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |).



object.__iadd__(self, other)
object.__isub__(self, other)
object.__imul__(self, other)
object.__imatmul__(self, other)
object.__itruediv__(self, other)
object.__ifloordiv__(self, other)
object.__imod__(self, other)
object.__ipow__(self, other[, modulo])
object.__ilshift__(self, other)
object.__irshift__(self, other)
object.__iand__(self, other)
object.__ixor__(self, other)
object.__ior__(self, other)


These methods are called to implement the augmented arithmetic assignments (+=, -=, *=, @=, /=, //=, %=, **=, <<=, >>=, &=, ^=, |=).






g__(self)
object.__pos__(self)
object.__abs__(self)
object.__invert__(self)
Called to implement the unary arithmetic operations (-, +, abs() and ~).






"""

class Currency:
    def __next__(self):
        self.n+=1
        if self.n>10:
            raise StopIteration
        return self.n

    def __iter__(self):
        self.n=1
        return self
    def manage(self, n):
        if n<10:
            return "0{0}".format(n)
        return "{0}".format(n)
    def __init__(self,rs,paise):
        self.n=1
        self.total = rs * 100 + paise
    def __str__(self):
        r = self.total // 100
        p = self.total % 100
        r=self.manage(r)
        p=self.manage(p)
        return "₹ {0}.{1}".format(r, p)
    def __add__(self, other):
        return Currency(0,self.total + other.total)
    def __gt__(self, other):
        return  self.total>other.total

c1 = Currency(1,12)
c2 = Currency(10,12)
print(c1)
print(c2)
sum = c1 + c2
print(sum)
if c1>c2:
    print(c1)
else:
    print(c2)
for x in c1:
    print(x)
>>>>>>> 56d7daca8a1ee55b1b74af47c72bc1e40ed5ebd6
