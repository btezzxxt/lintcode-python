class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        # Write your code here
        if not nums:
            return 0 
        
        dp = [1] * len(nums)
        count = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1 
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

        maxlen = max(dp)
        cnt = 0
        for i, val in enumerate(dp):
            if val == maxlen:
               cnt += count[i]
        return cnt