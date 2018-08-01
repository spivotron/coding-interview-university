class LinkedList(object):
    def __init__(self, head= None):
        self.value = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current  = current.next
            current.next = new_element
        else:
            self.head = new_element
