import sys
class Solution:
    """
    @param matrix: an integer array of n * m matrix
    @param k: An integer
    @return: the maximum number
    """
    def maxSlidingMatrix(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])

        if m < k or n < k:
            return 0

        sum_prefix = [[0 for _ in range(n)] for _ in range(m)]
        sum_prefix[0][0] = matrix[0][0]
        for i in range(1, n):
            sum_prefix[0][i] = sum_prefix[0][i - 1] + matrix[0][i]
        
        for i in range(1, m):
            sum_prefix[i][0] = sum_prefix[i - 1][0] + matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                sum_prefix[i][j] = sum_prefix[i - 1][j] + sum_prefix[i][j - 1] + matrix[i][j] - sum_prefix[i - 1][j - 1]

        maxi = -sys.maxsize
        for i in range(k - 1, m):
            for j in range(k - 1, n):
                cur_sum = sum_prefix[i][j]
                if i - k >= 0:
                    cur_sum -= sum_prefix[i - k][j]
                
                if j - k >= 0:
                    cur_sum -= sum_prefix[i][j - k]

                if i - k >= 0 and j - k >= 0:
                    cur_sum += sum_prefix[i - k][j - k]

                maxi = max(maxi, cur_sum)

        return maxi


           