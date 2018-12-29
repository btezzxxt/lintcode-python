from collections import deque
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x):
        # write your code here
        if not self.q1:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
        else:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())


    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if self.q1:
            return self.q1.popleft()
        else:
            return self.q2.popleft()

                

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self.q1:
            return self.q1[0]
        else:
            return self.q2[0]
    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.q1) == 0 and len(self.q2) == 0

