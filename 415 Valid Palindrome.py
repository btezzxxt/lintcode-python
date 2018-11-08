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