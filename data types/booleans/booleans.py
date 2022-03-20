



# A short write up on the Python Boolean Data Type
"""
All objects in Python can be tested for True or False and can be used
 in an if or while condition or as operand of the Boolean operations below.
  The following values are considered false:

None
False
zero of any numeric type, for example, 0, 0.0, 0j.

any empty sequence, for example, '', (), [].

any empty mapping, for example, {}.

instances of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns the integer zero or bool value False. [1]

All other values are considered true — so objects of many types are always true.

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)


"""
# Here are some examples

if None:
    print("None True")
else:
    print("None False")
if False:
    print("False True")
else:
    print("True False")
if 0:
    print("0 True")
else:
    print("0 False")
if 0.0:
    print("0.0 True")
else:
    print("0.0 False")
if 0j:
    print("0j True")
else:
    print("0j False")
if '':
    print("'' True")
else:
    print("'' False")
if "":
    print('"" True')
else:
    print('"" False')
if ():
    print("() True")
else:
    print("() False")
if []:
    print("[] True")
else:
    print("[] False")
if {}:
    print("{} True")
else:
    print("{} False")


class A:
    def __len__(self):
        return 0


a = A()
if a:
    print("A True")
else:
    print("A False")


class B:
    def __bool__(self):
        return False


b = B()
if b:
    print("B True")
else:
    print("B False")
"""
Everything else is True
"""
"""
Boolean Operations — and, or, not¶
These are the Boolean operations, ordered by ascending priority:

Operation       	Result          	
x or y	            False if all inputs are False, else True
x and y	            True if all inputs are True, else False
not x	            True if x is False, else True
Extra:

or and and are short-circuit operators,and evaluated only till the value is known
Any True value makes or stop and similarly for andd
not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

"""
"""Or"""
print(False or False)
print(False or True)
print(True or False)
print(True or True)
# Any combination works. The first True value is used if its exists otherwise the last False
print("[] or 0=", [] or 0)
print("{1} or []=", {1} or [])
print({1} or [1])
print([False] or 0)  # [False] is actually True

'''And'''
print(False or False)
print(False or True)
print(True or False)
print(True or True)
# Any combination works. The last False value is used if it exists otherwise the first True
print("[] and 0=", [] and 0)
print("{1} and []=", {1} and [])
print({1} and [1])
print([False] and 1)  # [False] is actually True

# Short Circuit Examples
# If you enter 0 for A then Python will ask for B otherwise it will not
print("OR")
print(int(input("Enter A")) or int(input("Enter B")))
print("AND")
# If you enter 1 for A then Python will ask for B otherwise it will not
print(int(input("Enter A")) and int(input("Enter B")))



