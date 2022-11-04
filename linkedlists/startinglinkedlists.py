"""
What is a linked list?
A linked list is a dynamic Data Structure in which each node contains a value and a
pointer to the next node.

"""


# Class for ListNode
class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


# Create a class to store the header node
class ListHeader:
    def __init__(self):
        self.head = None

    def addFirst(self, value):
        newnode = ListNode(value)
        newnode.next = self.head
        self.head = newnode

    def addLast(self, value):
        newnode = ListNode(value)
        if self.head is None:
            self.head = newnode
            return

        start = self.head
        while start.next is not None:
            start = start.next
        start.next = ListNode(value)

    def find(self, value):
        start = self.head
        while start is not None:
            if start.value == value:
                return "Found"
            start = start.next
        return "Not Found"

    def traverse(self):
        start = self.head
        while start is not None:
            print(start.value, end=",")
            start = start.next


if __name__ == '__main__':
    head = ListHeader()
    for i in range(1, 6):
        head.addLast(i)
    head.traverse()
    print(head.find(10))
    print(head.find(1))
