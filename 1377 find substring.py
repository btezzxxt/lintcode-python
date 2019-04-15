class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        # Write your code here
        if len(str) < k:
            return 0 
        
        l = 0 
        r = k - 1
        n = len(str)
        
        counted = set()
        while r < n:
            if self.check(str, l, r):
                counted.add(str[l: r + 1])
            l += 1 
            r += 1 
        return len(counted)
        
    def check(self, str, l, r):
        letters = [0] * 26 
        for i in range(l, r + 1):
            letter = str[i]
            if letters[ord(letter) - ord('a')] > 0:
                return False
            letters[ord(letter) - ord('a')] = 1 
        return True
                
            
            