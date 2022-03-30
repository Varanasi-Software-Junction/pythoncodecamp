"""
 Comparisons
There are eight comparison operations in Python.
They all have the same priority (which is higher than that of the Boolean operations).


This table summarizes the comparison operations:

Operation	Meaning
<	strictly less than
<=	less than or equal
>	strictly greater than
>=	greater than or equal
==	equal
!=	not equal
is	object identity
is not	negated object identity


"""
print("1<1", 1 < 1)
print("1<=1", 1 <= 1)
print("1<2 and 1<3", 1 < 2 and 2 < 3)
"""
Comparisons can be chained arbitrarily; for example, x < y <= z is equivalent to x < y and y <= z, except that y is evaluated only once (but in both cases z is not evaluated at all when x < y is found to be false).
"""
print("1<2<3", 1 < 2 < 3)  # Same as previous one
"""
Objects of different types, except different numeric types, never compare equal. Furthermore, some types (for example, function objects) support only a degenerate notion of comparison where any two objects of that type are unequal. The <, <=, > and >= operators will raise a TypeError exception when comparing a complex number with another built-in numeric type, when the objects are of different types that cannot be compared, or in other cases where there is no defined ordering.

Non-identical instances of a class normally compare as non-equal unless the class defines the __eq__() method.

Instances of a class cannot be ordered with respect to other instances of the same class, or other types of object, unless the class defines enough of the methods __lt__(), __le__(), __gt__(), and __ge__() (in general, __lt__() and __eq__() are sufficient, if you want the conventional meanings of the comparison operators).

The behavior of the is and is not operators cannot be customized; also they can be applied to any two objects and never raise an exception.

Two more operations with the same syntactic priority, in and not in, are supported only by sequence types  list, tuple, range.

"""
