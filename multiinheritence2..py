class A:
    def f1(self):
        print('f1 in A')
class B(A):
    def f1(self):
        print('f1 in B')
    def f2(self):
        print('f2 in B')
o=B()
o.f1()