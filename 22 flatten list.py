class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        stack = [nestedList]
        res = []

        while stack:
            if isinstance(stack[-1], int):
                res.append(stack.pop())
            else:
                arr = stack.pop()
                for item in reversed(arr):
                    stack.append(item)
        return res