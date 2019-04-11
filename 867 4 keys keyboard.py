class Solution:
    """
    @param N: an integer
    @return: return an integer
    """
    def maxA(self, N):
        # write your code here
        dp = [0] * (N + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            # select all & copy
            dp[i] = i
            steps_left = i - 2
            # at least we need one A to print, so we could copy from 0 to steps_left -1 times
            for copy_times in range(0, steps_left):
                dp[i] = max(dp[i - 2 - copy_times] + dp[i - 2 - copy_times] * copy_times, dp[i])
        return dp[N]

print(Solution().maxA(5))
