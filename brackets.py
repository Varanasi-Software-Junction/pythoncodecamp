exp = "((a*)(b+c*(d+e)) (d-d)"
# print(len( exp[1:4]))
stack = []
output = []
n = len(exp)
for i in range(n):
    char = exp[i]
    if char == '(':
        stack = [i] + stack
    if char == ')':
        if len(stack) <= 0:
            continue
        pos = stack[0]
        del stack[0]
        expression = exp[pos:i + 1]
        print(expression)
