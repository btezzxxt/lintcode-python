class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        count = self.dfs(matrix, 0, len(matrix) - 1, 0, len(matrix[0]) - 1, target)
        return count
    
    # @return count
    def dfs(self, matrix, row_s, row_e, col_s, col_e, target):
        if row_s > row_e or col_s > col_e:
            return 0
        
        if row_s == row_e and col_s == col_e:
            if matrix[row_s][col_s] == target:
                return 1
            else:
                return 0
        
        row_mid = (row_s + row_e) // 2
        col_mid = (col_s + col_e) // 2 
        mid_val = matrix[row_mid][col_mid]
        if target <= mid_val:
            return self.dfs(matrix, row_s, row_mid, col_s, col_mid, target) \
                + self.dfs(matrix, row_mid + 1, row_e, col_s, col_mid, target) \
                + self.dfs(matrix, row_s, row_mid, col_mid + 1, col_e, target)
        else:
            return self.dfs(matrix, row_mid + 1, row_e, col_mid + 1, col_e, target) \
                + self.dfs(matrix, row_mid + 1, row_e, col_s, col_mid, target) \
                + self.dfs(matrix, row_s, row_mid, col_mid + 1, col_e, target)

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        i = m - 1 
        j = 0 
        
        count = 0
        while j < n and i >= 0:
            if matrix[i][j] == target:
                count += 1 
                i -= 1 
                j += 1 
            elif matrix[i][j] < target:
                j += 1 
            else:
                i -= 1 
                
        return count 
# O(n + m)