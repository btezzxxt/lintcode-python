import sys
class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        maxi, left_maxi, right_maxi = self.continuousSubarraySum(A)
        mini, left_mini, right_mini = self.continuousSubarraySumMini(A)
        total = sum(A)

        if right_mini + 1 >= len(A) or left_mini - 1 < 0:
            return [left_maxi, right_maxi]

        if maxi >= total - mini:
            return [left_maxi, right_maxi]
        else:
            return [right_mini + 1, left_mini - 1]


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
        return maxi, left, right

    def continuousSubarraySumMini(self, A):
        # write your code here
        if not A:
            return []
        
        dp = [(0, 0) for _ in range(len(A) + 1)]
        dp[0] = (0, -1)

        mini = sys.maxsize
        for i in range(1, len(A) + 1):
            index = i - 1
            if dp[i - 1][0] < 0:
                dp[i] = (dp[i - 1][0] + A[index], dp[i-1][1])
            else:
                dp[i] = (A[index], index - 1)

            if dp[i][0] < mini:
                mini = dp[i][0]
                left = dp[i][1] + 1
                right = index
        return mini, left, right

print(Solution().continuousSubarraySumII([-101,-33,-44,-55,-67,-78,-101,-33,-44,-55,-67,-78,-100,-200,-1000,-22,-100,-200,-1000,-22]))