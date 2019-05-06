class Solution:
    """
    @param x: a number
    @return: return the next sparse number behind x
    """
    def nextSparseNum(self, x):
        # write your code here
        original = x
        ones = 0
        for i in range(32):
            temp = 1 << i 
            if x & temp and x & (temp << 1):
                x += temp 
            elif x & temp:
                ones += temp

        for i in range(31, -1, -1):
            temp = 1 << i
            if ones & temp and x - temp >= original:
                x -= temp 
        return x
                
        
        