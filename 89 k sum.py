class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        m = len(A)
        dp = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(m + 1)]

        # init
        for i in range(m + 1):
            dp[i][0][0] = 1

        # first i nums in A
        for i in range(1, m + 1):
            # pick first j within k
            for j in range(1, k + 1):
                if j > i:
                    continue
                for t in range(target + 1):
                    if t - A[i - 1] >= 0:
                        dp[i][j][t] = dp[i-1][j][t] + dp[i-1][j-1][t-A[i-1]]
                    else:
                        dp[i][j][t] = dp[i-1][j][t]
        return dp[m][k][target]

print(Solution().kSum([1,2,3,4], 2, 5))