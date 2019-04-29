"""
Example 1:

Input: [4, 14, 2]
Output: 6
Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Example 2:

Input: [2, 1, 0]
Output: 4
Explanation: In binary representation, the 2 is 10, 1 is 01, and 0 is 00 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(2, 1) + HammingDistance(1, 0) + HammingDistance(2, 0) = 2 + 1 + 1 = 4.
"""

class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """
    def totalHammingDistance(self, nums):
        # Write your code here
        total = 0
        for i in range(32):
            one_pos = 1 << i 
            ones = 0
            zeros = 0
            for num in nums:
                if num & one_pos:
                    ones += 1 
                else:
                    zeros += 1
            total += ones * zeros
        return total