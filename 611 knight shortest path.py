class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if len(grid) == 0 or len(grid[0]) == 0:
            return -1

        dx = [1, 1, -1, -1, 2, 2, -2, -2]
        dy = [2, -2, 2, -2, 1, -1, 1, -1]

        start = (source.x, source.y)
        queue = deque([start])

        distance = {}
        distance[start] = 0

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == (destination.x, destination.y):
                    return distance[cur]
                
                for i in range(len(dx)):
                    nextX = cur[0] + dx[i]
                    nextY = cur[1] + dy[i]
                    nxt = (nextX, nextY)
                    if 0 <= nextX and nextX < len(grid) and 0 <= nextY and nextY < len(grid[0]) and grid[nextX][nextY] == 0:
                        if nxt not in distance:
                            queue.append(nxt)
                            distance[nxt] = distance[cur] + 1
        return -1

print(Solution().shortestPath([[0,0,0,0,1,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,1,0,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1]],Point(0,0),Point(7,0)))

