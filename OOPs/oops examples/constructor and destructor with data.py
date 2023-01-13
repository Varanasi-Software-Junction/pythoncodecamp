# Constructor and Destructor
class A:
    def __init__(self, data=None):
        self.data = data
        print("Constructor Called " + data)

    def __del__(self):
        print("Destructor Called " + self.data)


a = A("One")
b = A("Two")
