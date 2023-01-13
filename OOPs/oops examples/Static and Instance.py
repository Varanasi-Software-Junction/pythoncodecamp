class StaticAndInstanceDemo:

    @staticmethod
    def IamStaticMethod():
        print("Static Method")

    def IamInstanceMethod(self):
        print("Instance Method")
        self.IamInstanceVariable = "Instance Variable"

    IamStaticVariable = "Static Value"


StaticAndInstanceDemo.IamStaticMethod()
print(StaticAndInstanceDemo.IamStaticVariable)
a=StaticAndInstanceDemo()
a.IamInstanceMethod()
print(a.IamInstanceVariable)