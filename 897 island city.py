class Solution:
    """
    @param grid: an integer matrix
    @return: an integer 
    """
    count = 0
    def numIslandCities(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0 
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] != 0:
                    self.dfs(grid, i, j, visited, [False])
        return self.count
        
    def dfs(self, grid, i, j, visited, found_city):
        visited.add((i, j))
        
        if grid[i][j] == 2 and not found_city[0]:
            self.count += 1 
            found_city[0] = True
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        m = len(grid)
        n = len(grid[0])
        
        for k in range(4):
            di = i + dx[k]
            dj = j + dy[k]
            
            if di >= 0 and di < m and dj >= 0 and dj < n and (di, dj) not in visited and grid[di][dj] != 0:
                self.dfs(grid, di, dj, visited, found_city)
                
print(Solution().numIslandCities([[0,1,2,0],[1,1,1,0],[2,0,1,1]]))


# [0,1,2,0],
# [1,1,1,0],
# [2,0,1,1]