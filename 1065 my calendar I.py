class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end 
        self.left = None
        self.right = None 
    
    def add(self, start, end):
        if start >= self.end:
            if not self.right:
                self.right = Node(start, end)
                return True
            else:
                return self.right.add(start, end)
        elif end <= self.start:
            if not self.left:
                self.left = Node(start, end)
                return True 
            else:
                return self.left.add(start, end)
        else:
            return False

class MyCalendar:

    def __init__(self):
        self.dummy = Node(-1, -1)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        return self.dummy.add(start, end)
        