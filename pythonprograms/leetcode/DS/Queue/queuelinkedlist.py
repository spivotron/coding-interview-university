class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
    def __repr__(self):
        return repr(self.value)

class QueueLL:
    def __init__(self):
        self.head = self.tail =  None

        self.size = 0

    def enQueue(self,value):
        newNode = Node(value)
        if self.tail is not None:
            self.tail.next = newNode
        else:
            self.head = Node(value)
        self.tail = newNode
        self.size += 1
        # current = self.head
        # if self.head:
        #     while current.next:
        #         current = current.next
        #     current = Node(value)
        # else:
        #     self.head = Node(value)
        # self.size += 1

    def deQueue(self):
        if self:
            self.head = self.head.next
            self.size -= 1
        else:
            raise EmptyQueue()
        # if self.head:
        #     oldHead =self.head
        #     self.head = self.head.next
        #     return oldHead
        # else:
        #     self.head = None;
        # return None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def empty(self):
        return self.head == None

    def getSize(self):
        return self.size

    def __bool__(self):
        return not (self.head is None and self.tail is None)

    def __contains__(self, value):
        return value in (node.data for node in self)

    def __len__(self):
        return self.count
    def __repr__(self):
        return 'Queue<{nodes}>'.format(nodes=', '.join(repr(node) for node in self))

class EmptyQueue(Exception):
    pass

test_list = [1, 2, 3, 4, -2000000, 'a', 500000, 50]
MyQueue = QueueLL()
for i in test_list:
    MyQueue.enQueue(i)
print(MyQueue.getSize())
print(MyQueue)
