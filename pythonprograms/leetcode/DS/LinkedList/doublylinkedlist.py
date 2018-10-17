class Node(object):
    def __init__(self, value):
        self.value = value
        self.next, self.prev = None, None

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
        newNode = Node(val)
        # print(self.head.value)
        self.head = newNode
        newNode.next = self.head

        self.size  += 1
        # newNode = current


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        current = self.head
        newNode = Node(val)

        if current:
            print(Node(current.next).value)
            # while current.next != None:
            #     current = current.next
            # current.next = newNode
            # newNode = current
        else:
            self.head = newNode

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
            current.next = newNode
            newNode.prev = current

            newNode.next = current.next
            current.next.prev = newNode

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
                current.next.prev = current.prev
            else:
                return
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# obj.addAtIndex(0,1)
obj.addAtHead(2)
# print(obj.get(0))
obj.addAtTail(2)

# print(obj.get(1))

# obj.addAtIndex(i,val)
# obj.deleteAtIndex(index)