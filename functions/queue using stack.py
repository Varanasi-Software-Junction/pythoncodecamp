class Stack():
    def __init__(self):
        self.data=[]
    def push(self,data):
        self.data.append(data)
    def pop(self):
        if len(self.data)<=0:
            return None
        return self.data.pop()
    def empty(self):
        return len(self.data)<=0
class Queue():
    def __init__(self):
        self.st1=Stack()
        self.st2=Stack()
        self.direction=1
    def enque(self,data):
        if self.direction==1:
            self.st1.push(data)
            return
        else:
            while not st2.empty():
                x=st2.pop()
                st1.push(x)
            self.st1.push(data)
            self.direction=1
    def deque(self):
        if self.direction==2:
            # if len(self.)
            pass

s1=Stack()
for i in range(5):
    s1.push(i)
while not s1.empty():
    print(s1.pop())