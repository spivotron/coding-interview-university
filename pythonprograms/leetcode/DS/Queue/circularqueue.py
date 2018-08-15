class CircularQueue(object):
    def __init__(self, k):
        self.size = k
        self.data = [None]*k
        self.head = -1
        self.tail = -1

    def enQueue(self,value):
        if self.isEmpty():
            self.data[0]  =value
            self.head = 0
            self.tail = 0
            return True
        elif self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.size
            self.data[self.tail] = value
            return True
    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            self.data[self.head] = None

            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.size
            return True

    def Rear(self):
        return -1 if self.isEmpty() else self.data[self.tail]

    def Front(self):
        return -1 if self.isEmpty() else self.data[self.head]

    def isEmpty(self):
        return self.head == -1 and self.tail == -1

    def isFull(self):
        return self.head == (self.tail + 1) % self.size
