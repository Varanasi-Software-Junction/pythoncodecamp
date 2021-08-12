class A:
    def f1(self):
        print("F1 in A")
class B:
    def f2(self):
        print("F2 in B")
    def f1(self):
        print("F1 in B")
class C(A,B):
    def f(self):
        A().f1()
        B().f1()
        

c = C()
c.f1()
c.f2()
c.f()
