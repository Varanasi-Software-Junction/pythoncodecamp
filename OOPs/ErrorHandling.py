class AgeException(Exception):
    def __init__(self, message):
        Exception.__init__(self,message)

try: # Write the code whose exceptions need handling
    d={1:"One"}
    print(d[1])
    x=int("1")
    age=int(input("Age\n"))
    if age < 0:
        raise AgeException("Age is -ve")#Throw your own exception

except KeyError as  error_message:#Handle the key errors
    print("Key Error " + str(error_message))
except ValueError as v:
    print("Value Error " + str(v))
except ZeroDivisionError as manas:
    print(manas)
except Exception as e:#All Remaining Exceptions
    print(e)
else:#If no exception occured
    print("All correct")
finally:#Runs everytime in the end
    print("Bye ")