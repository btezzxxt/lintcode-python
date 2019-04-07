# from heapq import heappop, heappush, heappushpop
# class Cell:
#     def __init__(self, x, y, val):
#         self.x = x
#         self.y = y
#         self.val = val

#     def __lt__(self, other):
#         return self.val < other.val

#     def __eq__(self, other):
#         return self.val == other.val

# class Solution:
#     """
#     @param heights: a matrix of integers
#     @return: an integer
#     """
#     def trapRainWater(self, heights):
#         # write your code here
#         if len(heights) == 0 or len(heights[0]) == 0:
#             return 0
#         minheap = []

#         m = len(heights) 
#         n = len(heights[0]) 

#         visited = [[0] * n for i in range(m)] 

#         for i in range(n):
#             cellTop = Cell(0, i, heights[0][i])
#             cellBot = Cell(m-1, i, heights[m-1][i])   
#             heappush(minheap, cellTop)
#             heappush(minheap, cellBot)
#             visited[0][i] = 1
#             visited[m-1][i] = 1

#         for i in range(1, m - 1):
#             cellLeft = Cell(i, 0, heights[i][0])
#             cellRight = Cell(i, n-1, heights[i][n-1])  
#             heappush(minheap, cellLeft)
#             heappush(minheap, cellRight)
#             visited[i][0] = 1
#             visited[i][n-1] = 1
        
#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, 1, -1]

#         total = 0
#         while minheap:
#             cur = heappop(minheap)
#             for i in range(4):
#                 newX = cur.x + dx[i]
#                 newY = cur.y + dy[i]
#                 if newX < m and newX >= 0 and newY < n and newY >= 0 and visited[newX][newY] == 0:
#                     newHeight = heights[newX][newY]
#                     visited[newX][newY] = 1
#                     total += max(cur.val - newHeight, 0)
#                     newCell = Cell(newX, newY, max(newHeight, cur.val)) # 这个max比较关键 一直以最高的墙壁为界限计算
#                     heappush(minheap, newCell)
        
#         return total
                
# print(Solution().trapRainWater([[45,92,47,47,53,79],[11,95,21,7,57,2],[59,98,57,58,70,8],[28,90,14,95,91,24],[44,43,25,19,9,18]]))

        
class PointNode:
    def __init__(self, height, i, j):
        self.h = height
        self.x = i 
        self.y = j
    
    def __lt__(self, other):
        return self.h < other.h

from heapq import heappop, heappush
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights or not heights[0]:
            return 0
        
        heap = []
        visited = set()
        self.init(heights, heap, visited)
        
        m = len(heights)
        n = len(heights[0])
        
        water = 0
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        
        while heap:
            p = heappop(heap)
            print(p.h, p.x, p.y)
            for i in range(4):
                x = p.x + dx[i]
                y = p.y + dy[i]
                if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in visited:
                    water += max(0, p.h - heights[x][y])
                    self.add(visited, heap, x, y, max(p.h, heights[x][y]))
        return water
            
    def init(self, heights, heap, visited):
        m = len(heights)
        n = len(heights[0])
        
        for i in range(n):
            self.add(visited, heap, 0, i, heights[0][i])
            self.add(visited, heap, m - 1, i, heights[m - 1][i])
            
        for i in range(m):
            self.add(visited, heap, i, 0, heights[i][0])
            self.add(visited, heap, i, n - 1, heights[i][n - 1])
    
    def add(self, visited, heap, x, y, height):
        if (x, y) not in visited:
            p = PointNode(height, x, y)
            heappush(heap, p)
            visited.add((x, y))