from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    # bfs 经典题
    def shortestPath2(self, grid):
        # write your code here
        dx = [-1, 1, 2, -2]
        dy = [2, 2, 1, 1]
        
        queue = deque([(0, 0)])
        target = (len(grid) - 1, len(grid[0]) - 1)
        
        visited = set((0, 0))
        
        step = -1
        while queue:
            step += 1 
            for _ in range(len(queue)):
                (i, j) = queue.popleft()
                if (i, j) == target:
                    return step
                
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if (x, y) not in visited and x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] != 1:
                        queue.append((x, y))
                        visited.add((x, y))
        return -1
        