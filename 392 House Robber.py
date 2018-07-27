class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        
        if len(A) == 1:
            return A[0]
        
        f = [0] * len(A)
        f[0] = A[0]
        f[1] = max(A[0], A[1])

        for i in range(2, len(A)):
            f[i] = max(f[i-2] + A[i], f[i-1])
        
        return f[i]