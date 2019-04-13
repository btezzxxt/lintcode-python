class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        count = 0
        island = set()
        
        for i in range(m):
            for j in range(n):
                if self.is_valid(grid, i, j):
                    path = []
                    self.dfs(grid, i, j, path, i, j)
                    id = str(path)
                    if id not in island:
                        island.add(id)
                        count += 1 
        return count
                
    def dfs(self, grid, i, j, path, bi, bj):
        grid[i][j] = '*'
        path.append((i - bi, j - bj))
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]            
            if self.is_valid(grid, x, y):
                self.dfs(grid, x, y, path, bi, bj)      
        
    def is_valid(self, matrix, i, j):
        m = len(matrix)
        n = len(matrix[0])
        
        if i >= 0 and i < m and j >= 0 and j < n:
            if matrix[i][j] == 1:
                return True 
        return False
