class AgeError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


try:  # Write the code whose exceptions need handling
    d = {1: "One"}
    print(d[1])
    age = int(input("Enter Age: "))
    if age < 0:
        raise AgeError('Age is Negative')  # Throw your own exception
    f = 100 / 2

except KeyError as e:  # Handling Key Errors
    print("Key Error " + str(e))
except ValueError as v:  # Handling Value Errors
    print('Value Error ' + str(v))
except AgeError as f:  # Handling All remaining Excetions
    print("Age Error " + str(f))
except Exception as f:  # Handling All remaining Excetions
    print("Unknown Error " + str(f))
else:  # If no Exception occured
    print("No Exception Occurred")

finally:  # Runs Everytime in the end
    print("Bye")
