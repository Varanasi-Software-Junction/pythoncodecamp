class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def pop(self):
        if not self.head:
            return None
        value = self.head.data
        next = self.head.next
        del self.head
        self.head = next
        return value

    def empty(self):
        return not self.head


st = Stack()
for i in range(5):
    st.push(i)
while not st.empty():
    print(st.pop())
