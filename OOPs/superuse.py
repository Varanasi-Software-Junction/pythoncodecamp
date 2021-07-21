class A:
    def f(self):
        print("F in A")
class B:
    def f(self):
        print("F in B")
class C(B,A):
    def f(self):
        super(B,self).f()


c = C()
c.f()
