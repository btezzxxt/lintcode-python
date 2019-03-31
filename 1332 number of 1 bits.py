class Solution:
    """
    @param n: an unsigned integer
    @return: the number of â1' bits
    """
    def hammingWeight(self, n):
        # write your code here
        total = 0
        while n > 0:
            total += n & 1
            n >>= 1 
        return total