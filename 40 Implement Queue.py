class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.helper = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.helper:
            return self.helper.pop()
        else:
            while self.stack:
                self.helper.append(self.stack.pop())
            return self.helper.pop()
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self.helper:
            return self.helper[-1]
        else:
            while self.stack:
                self.helper.append(self.stack.pop())
            return self.helper[-1]
