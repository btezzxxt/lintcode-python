class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        
        max_ = 1
        cur = 0
        
        for i in range(len(A)):
            if i == 0:
                cur = 1 
            else:
                if A[i] > A[i-1]:
                    cur += 1 
                    max_ = max(max_, cur)
                else:
                    cur = 1 
        
        for i in range(len(A)-1, -1, -1):
            if i == len(A)-1:
                cur = 1 
            else:
                if A[i+1] < A[i]:
                    cur += 1 
                    max_ = max(max_, cur)
                else:
                    cur = 1 
        return max_



print(Solution().longestIncreasingContinuousSubsequence([5,4,3,2,1,3]))