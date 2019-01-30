"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.hasNext():
            return self.stack.pop().getInteger()
        else:
            return None

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            else:
                top = self.stack.pop()
                arr = top.getList()
                for item in reversed(arr):
                    self.stack.append(item)
        return False
        
