class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        # do intialization if necessary
        m = len(matrix)
        n = len(matrix[0])
        
        sum_matrix = [[0 for i in range(n + 1)] for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sum_matrix[i][j] = sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1] + matrix[i -1][j - 1]
        self.sum_matrix = sum_matrix
    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        # write your code here
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row1][col2 + 1] - self.sum_matrix[row2 + 1][col1] + self.sum_matrix[row1][col1]
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)