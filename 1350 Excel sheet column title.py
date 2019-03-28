class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n) -> str:
        # write your code here
        if n <= 0:
            return None
        
        res = ""
        while n > 0:
            n = n - 1
            remain = n % 26
            res = chr(ord("A") + remain) + res
            n = n // 26
            
        return res 
        
Solution().convertToTitle(5) # 'E'
Solution().convertToTitle(27) # 'AA'

            
            
            
                