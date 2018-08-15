"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0) # causes Theta(n) performance

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print()
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print (q.dequeue())
# Should be 3
print (q.dequeue())
# Should be 4
print (q.dequeue())
q.enqueue(5)
# Should be 5
print (q.peek())


class EfficientQueue(object):
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*DEFAULT_CAPACITY
        self._size = self.front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self.front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self.front]
        self._data[self.front] = None
        self.front  = (self.front + 1) % len(self._data)
        self._size -= 1
        return answer
    def enqueue(self,e):
        if self._size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    def resize(self, cap):
        old = self._data
        self._data= [None]*cap
        walk = self.front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk) % len(old)
        self.front = 0
