class FirstClass(object):
    def __init__(self):
        super(FirstClass, self).__init__()
        print("First Class Constructor")


class SecondClass(object):
    def __init__(self):
        super(SecondClass, self).__init__()
        print("Second Class")


class ThirdClass(FirstClass, SecondClass):
    def __init__(self):
        super(ThirdClass, self).__init__()
        print("Third Class")


obj = ThirdClass()
print(obj)
