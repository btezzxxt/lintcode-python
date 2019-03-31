class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    _ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def romanToInt(self, s):
        # write your code here
        if s == "":
            return 0 
        
        cur = self._ROMAN[s[-1]]
        total = cur 
        for i in range(len(s) - 2, -1, -1):
            if self._ROMAN[s[i]] < cur:
                total -= self._ROMAN[s[i]]
            else:
                total += self._ROMAN[s[i]]
            cur = self._ROMAN[s[i]]
            
        return total
