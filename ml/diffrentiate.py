import sympy
x = sympy.symbols('x')
exp = -3** x
exp = sympy.expand(exp)
print("Expression = {0}".format(exp))
dif = sympy.diff(exp, x)

print("Derivative = {0}".format(dif))