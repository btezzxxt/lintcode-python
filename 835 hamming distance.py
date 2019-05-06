class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        dis = 0
        for i in range(32):
            temp = 1 << i 
            if temp & x != temp & y:
                dis += 1 
        return dis