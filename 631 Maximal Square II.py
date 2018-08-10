class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def maxSquare2(self, matrix):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])

        f = [[0] * n for i in range(m)]
        g = [[0] * n for i in range(m)]
        h = [[0] * n for i in range(m)]
        max_ = 0

        for i in range(n):
            if matrix[0][i] == 1:
                f[0][i] = 1
                max_ = 1
        
        for i in range(m):
            if matrix[i][0] == 1:
                f[i][0] = 1
                max_ = 1
        
        for i in range(n):
            if matrix[0][i] == 0:
                g[0][i] = 1
        
        for i in range(m):
            if matrix[i][0] == 0:
                g[i][0] = 1
                
        for i in range(n):
            if matrix[0][i] == 0:
                h[0][i] = 1
        
        for i in range(m):
            if matrix[i][0] == 0:
                h[i][0] = 1                

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    f[i][j] = min(f[i-1][j-1], g[i-1][j], h[i][j-1]) + 1
                    g[i-1][j] = 0
                    h[i][j-1] = 0                 
                else:
                    g[i][j] = g[i-1][j] + 1
                    h[i][j] = h[i][j-1] + 1
                max_ = max(f[i][j], max_)

        
        return max_ * max_