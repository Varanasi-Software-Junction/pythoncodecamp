def matchParenthesis(expression, startposition):
    maxlength = 0
    tmp = expression[startposition:]
    st = []
    n = len(tmp)
    for i in range(n):
        ch = tmp[i]
        if (ch == "("):
            st.append(i)
            continue
        if (ch == ")"):
            if (len(st) <= 0):
                return tmp[:i]
            left = st.pop()
            newlength = i
            if newlength > maxlength:
                maxlength = newlength
            # print(tmp[left:i+1])
    return tmp


s = "(A+B)( C + D))(B*C)"
result = matchParenthesis(s, 0)

print(result)
result = matchParenthesis(s, 14)

print(result)
