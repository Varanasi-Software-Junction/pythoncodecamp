class A:
    def f1(self):
        print("F1 in A")

    def f2(self):
        print("F2 in A")


class B(A):
    def f1(self):
        print("F1 in B")
        super().f1()


b = B()
b.f1()
b.f2()
