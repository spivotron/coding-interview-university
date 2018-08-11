class Node(object):
  def __init__(self):
    self.val = None
    self.next = None
    self.prev = None

class DoubleLinkedList(object):
  def __init__(self, head=None):
    self.head = head
    self.size = 0


# add operation
"""
prev, cur, next

prev.next = cur
cur.next = next

cur.prev = prev
next.prev = cur
"""

# delete operation
"""
prev, cur, next

cur.prev.next = cur.next
cur.next.prev = cur.prev
"""

