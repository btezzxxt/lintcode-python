class Solution:
    """
    @param s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        # write your code here
        char_in_s = set()
        char_dup = set()
        for char in s:
            if char not in char_in_s:
                char_in_s.add(char)
                continue
            
            if char in char_in_s:
                char_dup.add(char)
        
        for i, char in enumerate(s):
            if char not in char_dup:
                return i 
        return -1
