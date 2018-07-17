from heapq import heappop, heappush, heappushpop
class Cell:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if len(heights) == 0 or len(heights[0]) == 0:
            return 0
        minheap = []

        m = len(heights) 
        n = len(heights[0]) 

        visited = [[0] * n for i in range(m)] 

        for i in range(n):
            cellTop = Cell(0, i, heights[0][i])
            cellBot = Cell(m-1, i, heights[m-1][i])   
            heappush(minheap, cellTop)
            heappush(minheap, cellBot)
            visited[0][i] = 1
            visited[m-1][i] = 1

        for i in range(1, m - 1):
            cellLeft = Cell(i, 0, heights[i][0])
            cellRight = Cell(i, n-1, heights[i][n-1])  
            heappush(minheap, cellLeft)
            heappush(minheap, cellRight)
            visited[i][0] = 1
            visited[i][n-1] = 1
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]

        total = 0
        while minheap:
            cur = heappop(minheap)
            for i in range(4):
                newX = cur.x + dx[i]
                newY = cur.y + dy[i]
                if newX < m and newX >= 0 and newY < n and newY >= 0 and visited[newX][newY] == 0:
                    newHeight = heights[newX][newY]
                    visited[newX][newY] = 1
                    total += max(cur.val - newHeight, 0)
                    newCell = Cell(newX, newY, max(newHeight, cur.val)) # 这个max比较关键 一直以最高的墙壁为界限计算
                    heappush(minheap, newCell)
        
        return total
                
print(Solution().trapRainWater([[45,92,47,47,53,79],[11,95,21,7,57,2],[59,98,57,58,70,8],[28,90,14,95,91,24],[44,43,25,19,9,18]]))

        
