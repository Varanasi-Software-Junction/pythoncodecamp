"""
Python functions accept input parameters.
Parameters are defined inside the brackets in the function definition.

This function has two parameters.
"""


def add(a, b):
    print("a=", a, ",b=", b)


# Both parameters are necessary
# add(9), add(1,2,3) are errors
"""
Default value parameters

"""


def d1Add(a, b=0):  # b is 0 if not given
    print("a=", a, ",b=", b)


add(1, 2)
d1Add(1, 2)
d1Add(2)  # B is 0


def d2Add(a=0, b=0):
    print("a=", a, ",b=", b)


d2Add(1, 2)
d2Add(1)
d2Add()
d2Add(b=7)  # Using a named parameter


def f1(*args):  # Pass a tuple as parameter
    print(type(args))
    for x in args:
        print(x, end=",")
    print()


def f2(**args):  # Pass a dictionary as parameter
    print(type(args))
    for key in args:
        print(key, "=", args[key], end=",")
    print()


f1(0, 2, 3)
f2(a=1, b=2, c=3)
"""
Return types
Python functions that don't return values explicitly have None
as return value
"""


def r1():  # None as return
    pass


print(r1(), type(r1()))


def r2():  # Int as return
    return 0


print(r2(), type(r2()))


def r3():  # Tuple as return
    return 1, 2


print(r3(), type(r3()))
