# class MyQueue:
#     """
#     @param: element: An integer
#     @return: nothing
#     """
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []

#     def push(self, x):
#         # write your code here
#         self.stack1.append(x)

#     """
#     @return: nothing
#     """
#     def pop(self):
#         # write your code here
#         if not self.stack2:
#             self._shuffle()
#         return self.stack2.pop()
                

#     """
#     @return: An integer
#     """
#     def top(self):
#         # write your code here
#         if not self.stack2:
#             self._shuffle()
#         return self.stack2[-1]
#     """
#     @return: True if the stack is empty
#     """
#     def isEmpty(self):
#         # write your code here
#         if not self.stack2:
#             self._shuffle()
#         return len(self.stack2) == 0

#     def _shuffle(self):
#         while self.stack1:
#             self.stack2.append(self.stack1.pop())


class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.s1.append(element)
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self.s2:
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self.s2:
            return self.s2[-1]
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]