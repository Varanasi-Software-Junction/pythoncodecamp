class A:
    def f1(self):
        print('f1 in A')

class B(A):
    def f1(self):
        print('f1 in B')

    def f1a(self):
        A().f1()
class C(B):
    def f1(self):
        print('f1 in c')
    def f1b(self):
        B().f1()
o = C()
o.f1()
o.f1a()
o.f1b()