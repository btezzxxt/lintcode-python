class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        l = 0
        r = x 
        while l < r:
            m = l - (l - r) // 2
            if m * m <= x and (m + 1) * (m + 1) > x:
                return m 
            elif m > x // m:
                r = m - 1 
            else:
                l = m + 1
        return l