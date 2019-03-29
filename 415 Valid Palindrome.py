import re
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if s == "":
            return True
        
        i = 0
        j = len(s) - 1

        while i < j:
            while not self.validLetter(s[i]) and i < j:
                i = i + 1
            while not self.validLetter(s[j]) and i < j:
                j = j - 1
            
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i = i + 1
                    j = j - 1
        return True

    def validLetter(self, letter):
        match = re.match(r'w', letter)
        if match:
            return True
        else:
            return False

print(Solution().isPalindrome('ab'))

import re
class Solution2:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if s == "":
            return True
        
        l = 0 
        r = len(s) - 1 
        while l < r:
            while l < r and not self.valid_letter(s[l]):
                l += 1 
            while l < r and not self.valid_letter(s[r]):
                r -= 1 
            if l < r:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1 
                    r -= 1 
        
        return True 
        
    def valid_letter(self, letter):
        if re.match(r"\w", letter):
            return True
        return False