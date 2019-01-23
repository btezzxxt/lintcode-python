import sys
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        if not A:
            return 0
        
        _, min_total = self.helper(A, 0, len(A) - 1, {})
        return min_total

    def helper(self, A, start, end, memo):
        if start == end:
            return A[start], 0

        if (start, end) in memo:
            return memo[(start, end)]

        min_total = sys.maxsize
        for i in range(start, end):
            left_val, left_total  = self.helper(A, start, i, memo)
            right_val, right_total = self.helper(A, i + 1, end, memo)
            add_val = left_val + right_val
            add_total = left_total + right_total + add_val
            min_total = min(min_total, add_total)

        memo[(start, end)] = add_val, min_total

        return memo[(start, end)]