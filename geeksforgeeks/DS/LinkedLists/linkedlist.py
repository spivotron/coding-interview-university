class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def sameLineTraversal(self):
        current = self.head
        while current:
            print current.data,  # python 2
            # print(current.data, end = " ") Python 3
            current = current.next

    def addAtFront(self, value):
        if self.head:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def addAtIndex(self, value, index):
        if self.head:
            current = self.head
            newNode = Node(value)
            for i in range(index - 1):
                current = current.next
            current.next = newNode
            newNode.next = current.next.next
        else:
            self.head = newNode

    def addAtTail(self, value):
        if self.head:
            current = self.head
            while current:
                current = current.next
            current.next = Node(val)
        else:
            self.head = Node(val)








ll = LinkedList()
ll.head = Node(1)
second = Node(2)
ll.head.next = second
second.next = Node(3)
ll.sameLineTraversal()
