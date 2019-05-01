class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        if not s:
            return True 
        
        l = 0 
        r = len(s) - 1 
        
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(s, l, r - 1)
            l += 1 
            r -= 1 
        return True
    
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1 
            end -= 1 
        return True 