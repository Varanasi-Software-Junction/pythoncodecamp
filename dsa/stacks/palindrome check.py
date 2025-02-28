'''
A
ABA
ABB
NITIN
MALAYALAM
MADAM



'''
'''
word = "    Madam   "
print(word, len(word))
word = word.lower().strip()
print(word, len(word))
word = word.upper()
print(word, len(word))

def push(st, value):
    # st.insert(0, value)
    st.append(value)

'''


def push(st, value):
    # st.insert(0, value)
    st.append(value)


def pop(st):
    if len(st) == 0:
        return None
    return st.pop()


def isEmpty(sst):
    if len(st) <= 0:
        return True
    return False


st = []
word = "   Mad1am   "
word = word.strip().lower()
print(word)
for ch in word:
    push(st, ch)
# print(st)
result = "Palindrome"
for ch in word:
    outch = pop(st)
    if ch != outch:
        result = "Not Palindrome"
        break
print(result)
