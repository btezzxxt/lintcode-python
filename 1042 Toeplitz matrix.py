class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if i + 1 >= m or j + 1 >= n:
                    continue
                
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
                
                    