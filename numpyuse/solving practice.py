from sympy import symbols, Eq, solve

x = symbols('x')
eq = Eq((x ** 2 - 9), 1)
print("Equation")
print(eq)

print(solve(eq, x))
