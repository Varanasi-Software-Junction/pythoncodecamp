class A:
    def f(self):
        print("F in A")
def addAll(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)
def f(*args):
    print(type(args))
    for arg in args:
        print(arg)
def ff(**kargs):
    print(type(kargs))
    for key,value in kargs.items():
        print(key,value)
f(1,2,3,4)
ff(name="pappu",age="10")

def f1():
    print("F1")
def f2():
    print("F2")
def sub(a,b):
    print(a-b)
def f(fn):
    fn()
    #print("F")
def fs(fn):
    fn(1,2)
    #print("F")
a=A()
fs(sub)
f(a.f)
addAll()