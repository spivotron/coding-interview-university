class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def rev_string(my_str):
    s = Stack()
    reversed = []
    for c in my_str:
        s.push(c)

    for i in range(s.size()):
        reversed.append(s.pop())
    return "".join(reversed)

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index] # current char
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def advanced_par_checker(symbol_string):
    s = Stack()
    balanced = True
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False
def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


m = Stack()
print(m.push('x'))
print(m.push('y'))
print(m.pop())
print(m.push('z'))
print(m.peek())


print(rev_string("henry"))

print(par_checker('((()))'))
print(par_checker('(()'))
