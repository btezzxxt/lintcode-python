class Solution:
    """
    @param matrix: the height matrix
    @param R: the row of (R,C)
    @param C: the columns of (R,C)
    @return: Whether the water can flow outside
    """
    def waterInjection(self, matrix, R, C):
        # Write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return "NO"
        
        if self.dfs(matrix, R, C, set()):
            return "YES"
        return "NO"
    
    def dfs(self, matrix, i, j, visited):
        if self.is_boarder(matrix, i, j):
            return True
        
        visited.add((i, j))
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        for k in range(4):
            di = i + dx[k]
            dj = j + dy[k]
            if self.is_valid(matrix, di, dj) and matrix[di][dj] <= matrix[i][j] and (di, dj) not in visited:
                if self.dfs(matrix, di, dj, visited):
                    return True
        return False
        
    def is_boarder(self, matrix, i, j):
        m = len(matrix)
        n = len(matrix[0])
        
        if (i == 0 or i == m - 1) or (j == 0 or j == n - 1):
            return True
        return False
        
    def is_valid(self, matrix, i, j):
        m = len(matrix)
        n = len(matrix[0])
        
        if 0 <= i and i < m and 0 <= j and j < n:
            return True
        return False
        
            