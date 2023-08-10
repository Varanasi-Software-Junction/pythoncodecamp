from sympy import symbols, Eq, solve, N
r = symbols('r', real=True)
emi = -100
p = 10
n = 5


eq = Eq(emi * ((1 + r) ** n - 1) - (p * r * (1 + r) ** n), 0)
print("Equation")
print(eq)
results = solve(eq, r)
for result in results:
    value = N(result)
    print(value)
