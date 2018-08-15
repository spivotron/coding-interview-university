class MyQueue(object):
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)
    def dequeue(self):
        self.data.pop(0)
    
