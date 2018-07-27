class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        s = [[0] * n for i in range(m)]

        max_ = 0
        for i in range(n):
            if matrix[0][i] == 1:
                max_ = 1
            s[0][i] = matrix[0][i]

        for i in range(m):
            if matrix[i][0] == 1:
                max_ = 1            
            s[i][0] = matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    s[i][j] = min(s[i-1][j-1], s[i][j-1], s[i-1][j])
                    max_ = max(max_, s[i][j])
        
        return max_ * max_
        