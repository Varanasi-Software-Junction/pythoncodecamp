class ageError(Exception):#Creating a new exception class
    def __init__(self,message):
        Exception.__init__(self,message)
class nameError(Exception):
    def __init(self,message):
        Exception.__init__(self,message)
class marksError(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

try:

    name = input('Enter Full Name :')
    if len(name)<4:
         raise nameError('Name is too short')

    for i in name:
        if (ord(i) not in range(65,91)) and  (ord(i) not in range(97,123) and ord(i) != 32):
            raise nameError('Name should not contain number or special character')

    age = int(input('Enter your age :'))
    if age < 0 or age >=60:
        raise ageError("Age is -ve or your age is greater than 60")

    pmarks = int(input('Enter your Physics Marks :'))
    if pmarks < 0 or pmarks > 100:
        raise marksError("Marks is not in between 0 and 100")
    cmarks = int(input('Enter your Chemsitry Marks :'))
    if cmarks < 0 or cmarks > 100:
        raise marksError("Marks is not in between 0 and 100")
except Exception as e:
    print("!!!!!!Registration Failed!!!!!!")
    print("Error : "+str(e))
else:
    print("--:Registered Sucessfully:--")
finally:
    print("Bye Bye")

