import sys
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        # write your code here
        if not A:
            return []
        
        dp = [(0, 0) for _ in range(len(A) + 1)]
        dp[0] = (0, -1)

        maxi = -sys.maxsize
        for i in range(1, len(A) + 1):
            index = i - 1
            if dp[i - 1][0] >= 0:
                dp[i] = (dp[i - 1][0] + A[index], dp[i-1][1])
            else:
                dp[i] = (A[index], index - 1)

            if dp[i][0] > maxi:
                maxi = dp[i][0]
                left = dp[i][1] + 1
                right = index
        return [left, right]
