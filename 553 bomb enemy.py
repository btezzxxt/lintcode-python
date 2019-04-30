class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    # brutal force TLE
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0 
            
        m = len(grid)
        n = len(grid[0])
        
        max_kill = 0
        for i in range(m):
            for j in range(n):
                kill = self.count_kill(grid, i, j)
                max_kill = max(kill, max_kill)
                
        return max_kill 
    
    def count_kill(self, grid, i, j):
        count = 0
        if grid[i][j] == 'E' or grid[i][j] == 'W':
            return count
        
        for k in range(i - 1, -1, -1):
            if grid[k][j] == 'W':
                break 
            
            if grid[k][j] == 'E':
                count += 1 
        
        for k in range(i + 1, len(grid)):
            if grid[k][j] == 'W':
                break 
            
            if grid[k][j] == 'E':
                count += 1 
        
        for k in range(j - 1, -1, -1):
            if grid[i][k] == 'W':
                break 
            
            if grid[i][k] == 'E':
                count += 1 
        
        for k in range(j + 1, len(grid[0])):
            if grid[i][k] == 'W':
                break 
            
            if grid[i][k] == 'E':
                count += 1 
                
        return count 
            
            
class Solution2:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0 
            
        m = len(grid)
        n = len(grid[0])
        
        counter = [[[0, 0, 0, 0] for i in range(n + 2)] for i in range(m + 2)]
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == 'W':
                    counter[i][j][0] = 0
                    counter[i][j][1] = 0
                elif grid[i - 1][j - 1] == 'E':
                    counter[i][j][0] = counter[i - 1][j][0] + 1
                    counter[i][j][1] = counter[i][j - 1][1] + 1
                else:
                    counter[i][j][0] = counter[i - 1][j][0]
                    counter[i][j][1] = counter[i][j - 1][1]
        
        max_kill = 0
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if grid[i - 1][j - 1] == 'W':
                    counter[i][j][2] = 0
                    counter[i][j][3] = 0
                    kill = 0
                elif grid[i - 1][j - 1] == 'E':
                    counter[i][j][2] = counter[i + 1][j][2] + 1 
                    counter[i][j][3] = counter[i][j + 1][3] + 1 
                    kill = 0
                else:
                    counter[i][j][2] = counter[i + 1][j][2]
                    counter[i][j][3] = counter[i][j + 1][3]
                    kill = counter[i - 1][j][0] + counter[i][j - 1][1] + counter[i + 1][j][2] + counter[i][j + 1][3]
                max_kill = max(max_kill, kill)
                
        return max_kill
                
            
            
                
            
            
            
            
            
                