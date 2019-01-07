class MyQueue:
    """
    @param: element: An integer
    @return: nothing
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        # write your code here
        self.stack1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if not self.stack2:
            self._shuffle()
        return self.stack2.pop()
                

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.stack2:
            self._shuffle()
        return self.stack2[-1]
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if not self.stack2:
            self._shuffle()
        return len(self.stack2) == 0

    def _shuffle(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
