class A:
    def f1(self):
        print("f1 in A")


class B:
    def f1(self):
        print("f1 in B")


class C(A, B):
    pass


c = C()
c.f1()
print(C.mro())
