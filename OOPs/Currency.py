"""
Starting a class that will be a complete example of Python OOPs
We will implement operator overloading as well.

The Currency class takes rupees and paise as input. Converts
paise >=100 into rupees and proceeds

"""
'''
Operators that can be overloaded

Operator. Required Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Methods
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)
Assignment Operators :
Operator	Method to be overloaded
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)
Unary Operators :
Operator	Method to be overloaded
–	__neg__(self)
+	__pos__(self)
~	__invert__(self)
Note: It is not possible to change the number of operands of an operator. For ex. you cannot overload a unary operator as a binary operator. The following code will throw a syntax error.




'''


class Currency:  # Starting a class declaration
    def __next__(self):  # Returs rupees the first time and paise the next time
        n = self.counter
        self.counter += 1
        if self.counter > 2:
            raise StopIteration

        if n == 0:
            return self.pad0(self.total // 100)
        return self.pad0(self.total % 100)

    def __iter__(self):
        self.counter = 0
        return self

    def pad0(self, n):  # Add leading 0 to numbers less than 10
        if n < 10:
            return "0{0}".format(n)
        return "{0}".format(n)

    def __init__(self, rs, paise):  # Constructor. Converts rs and paise to a total in paise and stores
        self.total = rs * 100 + paise

    def __str__(self):  # str function converts total to rupee and paise
        r = self.total // 100
        p = self.total % 100
        r = self.pad0(r)
        p = self.pad0(p)
        return "₹ {0}.{1}".format(r, p)

    def __add__(self, other):  # Implements the + operator
        return Currency(0, self.total + other.total)

    def __gt__(self, other):  # Implements the > operator
        return self.total > other.total

    def __le__(self, other):
        return self.total <= other.total

    def __getitem__(self, item):
        if item == 0:
            return self.pad0(self.total // 100)
        if item == 1:
            return self.pad0(self.total % 100)
        raise IndexError("list index out of range")

    def __len__(self):  # This is for a loop through sequence.We have two items rupees and paise
        return 2


c1 = Currency(1, 12)
print("C1 ", c1)
for i in c1:
    print(i)
c2 = Currency(2, -90)
print("C2 ", c2)
print("0", c2[0])
print("1", c2[1])
print(c1 <= c2)
