class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop(0)

    def is_empty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)
    def peek(self):
        return self.data[0]
    def size(self):
        return len(self.data)