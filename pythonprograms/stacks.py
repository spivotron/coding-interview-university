class ArrayStack:
    """LIFO stack implementation using a Python List as underlying storage"""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    """
    S.push(e)
    O(1)∗
    S.pop()
    O(1)∗
    S.top( )
    O(1)
    S.is empty()
    O(1)
    len(S)
    O(1)

    Space Usage for a stack is O(n)
    """
S = ArrayStack( )
S.push(5)
S.push(3)
print(len(S))
print(S.pop( ))
print(S.is_empty())
print(S.pop( ))
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top( ))
S.push(4)
print(len(S))
print(S.pop( ))
S.push(6)


# reversing data with a stack
def reverse_file(filename):
    S = ArrayStack()
    original = open(filename, 'r')
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()
# excersizes.  6.5, 6.6, 6.18, 6.17


# matching delimiters
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S= ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()
match = '[(5+x)-(y+z)]'
print(is_matched(match))


def is_matched_html(raw):
    S = ArrayStack()
    first = raw.find('<')
    while first != -1:
        next = raw.find('>',first+1)
        if next == -1:
            return False
        tag = raw[first+1:next] #this is the portion between the <>
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        next = raw.find('<', next+1)
    return S.is_empty()

html = "<body></body>"
print(is_matched_html(html))
