class A:
    def f1(self):
        print("F1 in A")

    def f2(self):
        print("F2 in A")


class B(A):
    def f1(self):
        print("F1 in B")



class C(A,B):
    def f1(self):
        print("F1 in C")



a = A()
a.f1()
a.f2()
b = B()
b.f1()
b.f2()
