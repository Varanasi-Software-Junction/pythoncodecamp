def push(st, value):
    # st.insert(0, value)
    st.append(value)


def pop(st):
    if len(st) == 0:
        return None
    return st.pop()
def isEmpty(sst):
    if len(st)<=0:
        return True
    return False

st = []
# st.append(1)
# print(st)
# st.append(2)
# print(st)
# st.insert(0,3)
# print(st)
# x=st.pop()
# print(x,st)

# for i in range(4):
#     push(st, i)
push(st, 1)
push(st, 2)
push(st, 3)
push(st, 4)

print(st)
while not isEmpty(st):
    x=pop(st)
    print(x)
# LIFO = Lats In First Out
#  Exp = (1+(2*(3+4)))
