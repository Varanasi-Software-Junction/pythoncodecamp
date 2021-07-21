class A:
    def f(self):
        print("F in A")
class B(A):
    def f(self):
        print( "F in B")
        A.f(self)
        super().f()
def add(a=0,b=0):
    print("A=",a,", B = ",b)
    return a + b
print(add(1,2))
print(add(2))
print(add())
print(add(b=9,a=8))
print(add(b=9))
a=A()
a.f()
a=B()
a.f()