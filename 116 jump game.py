class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        # dp
        dp = [0] * len(A)

        dp[0] = 1
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] == 1 and  j + A[j] >= i:
                    dp[i] = 1
        return dp[-1] == 1


print(Solution().canJump([1, 0]))
        # greedy algorithm
        # farest = 0
        # i = 0
        # while i <= farest:
        #     if A[i] + i > farest:
        #         farest = A[i] + i

        #     if farest >= len(A) - 1:
        #         return True
        #     i += 1
        
        # return False

        