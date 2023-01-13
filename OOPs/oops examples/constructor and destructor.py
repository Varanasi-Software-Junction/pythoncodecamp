# Constructor and Destructor
class A:
    def __init__(self):
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")


a = A()
