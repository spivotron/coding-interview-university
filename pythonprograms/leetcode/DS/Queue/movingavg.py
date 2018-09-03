from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.n = 0
        self.q = deque(maxlen = self.size)
        self.q.append(0)



    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        self.q.append(val)
        self.n +=1
        print(self.q)
        return float(sum(self.q))/self.n-1 if self.n > 1 else float(self.q[0])


m = MovingAverage(3);
m.next(1)
m.next(10)
m.next(3)


m.next(5)
