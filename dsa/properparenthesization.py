import stacks.Stack as stack

st = stack.Stack()
expression = "(a+b*(c-d)-e)"
result = "ok"
for ch in expression:
    if ch == '(':
        st.push(ch)
    if ch == ')':
        if st.empty():
            result = "invalid"
            break
        st.pop()
if not st.empty():
    result = "invalid"

print(result)
