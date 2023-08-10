from sympy import symbols, Eq, solve,N

x = symbols('x')
eq = Eq((x ** -2 + 9), 1)
print("Equation")
print(eq)
for result in solve(eq, x):
    print(N(result))
