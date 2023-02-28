class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.empty():
            return None
        return self.data.pop()

    def empty(self):
        return len(self.data) <= 0
