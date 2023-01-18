class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def empty(self):
        return not self.data


st = Stack()
for i in range(5):
    st.push(i)
while not st.empty():
    print(st.pop())
