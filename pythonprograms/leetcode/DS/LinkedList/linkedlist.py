class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self, head = None):
        """
        Initialize your data structure here.
        """
        self.head = head
        self.size = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1

        current = self.head
        for i in range(index):
            current = current.next
        return current.value
        # i = 0
        # if current:
        #     while i < index:
        #         if i == index:
        #             return current
        #         i+= 1
        #         current = current.next
        # else:
        #     return -1
        #

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        # current = self.head
        newNode= Node(val)
        newNode.next, self.head = self.head, newNode
        self.size  += 1
        # newNode = current


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Node(val)
        else:
            self.head = Node(val)

        self.size += 1



    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next # keep going next until you hit the next to last one from the index

            newNode = Node(val)
            newNode.next = current.next
            current.next = newNode
            self.size += 1

        # current = self.head
        # i = 0
        # newNode = Node(val)
        # if current:
        #     while current:
        #         if i == index - 1:
        #             current.next = newNode
        #             newNode.next = current.next
        #         i += 1
        #         current = current.next
        # else:
        #     current = Node(val)



    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            if current.next:
                current.next = current.next.next
            else:
                return
        self.size -= 1


    def getSize(self):
        return self.size


    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        # don't need this because it gets taken care of below
        # if head.next is None or head.next.next is None:
        #     return False
        else:
            current = head
            _next = head
            while _next is not None and _next.next is not None:
                current = current.next
                _next = _next.next.next

                if current == _next:
                    return True


    def detectCycle(self, head):
        nodes = set() # for maintaining a unique collection of Elements
        while head:
            if head in nodes:
                return head
            nodes.add(head)
            head = head.next
        return None

    def getIntersectionNode(self,headA, headB):
        l = []
        if headA is None or headB is None:
            return None
        while headA.next:
            l.append(headA.val)
            headA= headA.next
        l.append(headA.val)
        while headB:
            if headB in l:
                return headB
            elif headB.next:
                headB = headB.next
            else:
                return None

    def removeNthFromEnd(self, head, n):
        difference = self.length(head) - n
        if difference == 0:
            return head.next
        current = head
        for __ in range(difference - 1):
            current = current.next
        if current.next:
            nextNode = current.next.next
            current.next= nextNode
        elif current.next.next  == None:
            curent.next = None
        return head

    def length(self, head):
        size = 0
        current = head
        while current != None:
            current = current.next
            size +=1
        return size


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(0)
obj.addAtHead(1)
# obj.addAtHead(1)
obj.addAtTail(3)
print(obj.get(1))
obj.addAtIndex(1, 2)
print(obj.get(1))
obj.deleteAtIndex(1)
print(obj.get(1))
print("size is ", obj.getSize())
