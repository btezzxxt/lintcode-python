"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
class Celebrity:
    @classmethod
    def knows(self, a, b):
        return True

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        assume = 0
        for i in range(1, n):
            res = Celebrity.knows(i, assume)
            if not res:
                assume = i 
        
        for i in range(0, n):
            if i == assume:
                continue 
            if Celebrity.knows(assume, i) or not Celebrity.knows(i, assume):
                return -1 
        return assume