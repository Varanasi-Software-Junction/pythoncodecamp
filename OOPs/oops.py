class A:
    def f(self):
        print("F in A")
class B:
    def f(self):
        print("F in B")
class C(B,A):
    pass

c = C()
c.f()
