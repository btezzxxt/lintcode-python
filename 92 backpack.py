class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        A.sort()
        k = len(A)
        dp = [[False for _ in range(m + 1)] for _ in range(k + 1)]
        dp[0][0] = True
        for i in range(1, k + 1):
            for j in range(0, m + 1):
                case1 = dp[i - 1][j]
                left_space = j - A[i - 1]
                if left_space >= 0:
                    case2 = dp[i - 1][left_space]
                else:
                    case2 = False
                dp[i][j] = case1 or case2
        
        while m >= 0:
            if dp[k][m]:
                return m
            m -= 1
        return 0

print(Solution().backPack(11, [3, 4, 8, 5]))