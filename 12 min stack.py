class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.minStack = []
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.minStack:
            self.minStack.append(number)
        else:
            if self.minStack[-1] >= number:
                self.minStack.append(number)
        
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        number = self.stack.pop()
        if number == self.minStack[-1]:
            self.minStack.pop()
        return number

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        if self.minStack: 
            return self.minStack[-1]
        else:
            return None