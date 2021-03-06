"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id)
        # Run unit tests to check whether verison `id` is a bad version
        # return true if unit tests passed else false.
You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
bad version.
"""
class SVNRepo:
    @classmethod
    def isBadVersion(cls, id):
        if id >= 1:
            return True
        else:
            return False

class Solution:
    def findFirstBadVersion(self, n):
        # write your code here
        if n == 0:
            return 0 
            
        l = 1 
        r = n 
        while l + 1 < r:
            m = l + (r - l) // 2
            if SVNRepo.isBadVersion(m):  # use r
                r = m
            else:
                l = m 
        
        if SVNRepo.isBadVersion(l): #validate l first then r
            return l
        return r

print(Solution().findFirstBadVersion(31))

class Solution2:
    """
    @param: n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        l = 1 
        r = n 
        while l + 1 < r:
            m = (l + r) // 2
            if self.search_left(m):
                r = m 
            else:
                l = m 
        
        if SVNRepo.isBadVersion(l):
            return l 
        else:
            return r
    
    def search_left(self, seq):
        if SVNRepo.isBadVersion(seq):
            return True 
        
        return False