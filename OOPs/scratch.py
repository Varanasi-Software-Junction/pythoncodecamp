def f(*args):
    for arg in args:
        print(arg)
def ff(**kargs):
    for key,value in kargs.items():
        print(key,value)
f(1,2,3,4)
ff(name="pappu",age="10")