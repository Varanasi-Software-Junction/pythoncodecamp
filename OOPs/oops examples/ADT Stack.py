class Stack:
    def __init__(aman):
        aman.data = []

    def push(self, value):
        self.data.append(value)

    def pop(myself):
        if myself.data:
            return myself.data.pop()
        return None

    def empty(self):
        return not self.data


st = Stack()
for i in range(5):
    st.push(i)
while not st.empty():
    print(st.pop())
