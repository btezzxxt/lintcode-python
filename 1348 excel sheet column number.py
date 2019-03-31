class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        # write your code here
        bit = 0
        total = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            bit_value = ord(char) - ord('A') + 1 
            total += bit_value * pow(26, bit)
            bit += 1        
        return total