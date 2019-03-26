# # class UnionFind:
# #     def __init__(self):
# #         self.parent = {}
# #         self.count = 0

# #     def find(self, x):
# #         if self.parent[x] == x:
# #             return x
# #         self.parent[x] = self.find(self.parent[x])
# #         return self.parent[x]
    
# #     def union(self, a, b):
# #         root_a = self.find(a)
# #         root_b = self.find(b)
# #         if root_a != root_b:
# #             self.parent[root_a] = root_b
# #             self.count -= 1

# #     def add(self, x):
# #         self.parent[x] = x
# #         self.count += 1


# # class Solution:
# #     """
# #     @param grid: a boolean 2D matrix
# #     @return: an integer
# #     """
# #     def numIslands(self, grid):
# #         # write your code here
# #         uf = UnionFind()
# #         dx = [0, -1]
# #         dy = [-1, 0]

# #         n = len(grid)
# #         m = len(grid[0])

# #         for i in range(n):
# #             for j in range(m):
# #                 if grid[i][j] == 1:
# #                     uf.add(i * m + j)
# #                     for k in range(2):
# #                         new_i = i + dx[k]
# #                         new_j = j + dy[k]
# #                         if new_i >= 0 and new_i < n and new_j >=0 and new_j < m and grid[new_i][new_j] == 1:
# #                             uf.union(i * m + j, new_i * m + new_j)
# #         return uf.count


# #[[0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0],[0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0],[0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1],[1,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,0],[0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0],[0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,0,1],[0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1],[1,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1],[1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0],[1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1],[0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0],[1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0],[0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0],[0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1],[0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0],[1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0],[1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,1,0],[0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0],[0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0]]
# # 47

a = [
    [0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0],
    [0,1,0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0],
    [1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,0],
    [1,1,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,0,0],
    [0,1,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0],
    [0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,0,1],
    [1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,0],
    [0,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1],
    [0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,1],
    [0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0],
    [1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1],
    [1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1],
    [0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0]
]
# i = [
#     [0,0,0,0,0,0,1,1,0,0,0,0],
#     [0,0,0,0,0,0,1,1,0,0,0,0],
#     [0,0,0,0,0,1,0,1,1,1,1,0],
#     [0,0,1,0,0,1,1,1,1,1,1,1],
#     [0,1,1,1,1,0,1,0,0,0,0,0],
#     [0,1,0,1,0,0,1,0,0,0,0,0],
#     [1,1,1,0,0,1,1,0,0,0,0,0],
#     [1,0,1,1,0,1,1,0,0,1,0,0],
#     [0,0,0,0,0,0,0,1,1,1,0,0],
#     [0,0,0,0,0,0,0,1,0,1,1,0],
#     [0,0,0,0,0,0,1,1,1,1,0,0],
#     [0,0,0,0,0,0,1,0,0,1,0,0],
#     [0,0,0,0,0,0,1,1,1,0,0,0],
#     [0,0,0,0,0,0,0,1,1,0,0,0],
#     [0,0,0,0,0,0,0,0,0,1,1,0],
#     [0,0,0,0,0,0,0,0,0,0,1,1],
#     [0,0,0,0,0,0,0,0,0,0,1,1],
#     [0,0,0,0,0,0,0,0,0,1,0,1],
#     [0,0,0,0,0,0,0,0,1,1,1,1],
#     [0,0,0,0,0,0,0,0,0,1,0,0]
#     ]
# i2 = [
#     [0,0,0,0,0,0,1,1,0,0,0,0],
#     [0,0,0,0,0,0,1,1,0,0,0,0],
#     [0,0,0,0,0,1,0,1,1,1,1,0],
#     [0,0,1,0,0,1,1,1,1,1,1,1],
#     [0,1,1,1,1,0,1,0,0,0,0,0],
#     [0,1,0,1,0,0,1,0,0,0,0,0],
#     [1,1,1,0,0,1,1,0,0,0,0,0],
#     [1,0,1,1,0,1,1,0,0,0,0,0]
# ]

# print(Solution().numIslands(i))

# # bfs solution
# from collections import deque
# class Solution2:
#     """
#     @param grid: a boolean 2D matrix
#     @return: an integer
#     """
#     def numIslands(self, grid):
#         # write your code here
#         count = 0 
#         visited = {}
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1 and (i, j) not in visited:
#                     self.bfs_island(grid, i, j, visited)
#                     count += 1
#         return count
    
#     def bfs_island(self, grid, i, j, visited):
#         queue = deque([])
#         queue.append((i, j))
#         dx = [0, 0, -1, 1]
#         dy = [-1, 1, 0, 0]

#         while queue:
#             cur = queue.popleft()
#             visited[cur] = True
#             for j in range(4):
#                 x = cur[0] + dx[j]
#                 y = cur[1] + dy[j]
#                 if 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0]) and grid[x][y] and (x, y) not in visited:
#                     queue.append((x, y))

# union find solution
       
class UnionFind:
    def __init__(self):
        self.father = {}
        self.count = 0
    
    def visited(self, item):
        return item in self.father

    def add(self, item):
        if item not in self.father:
            self.father[item] = item
            self.count += 1

    def find(self, item):
        if self.father[item] == item:
            return item
        self.father[item] = self.find(self.father[item])
        return self.father[item]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1
    
    def get_count(self):
        return self.count

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        dx = [-1, 0]
        dy = [0, -1]

        uf_handle = UnionFind()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not uf_handle.visited((i, j)):
                    uf_handle.add((i, j))
                    for k in range(2):
                        x = i + dx[k]
                        y = j + dy[k]
                        if uf_handle.visited((x, y)):
                            uf_handle.union((i, j), (x, y))
        return uf_handle.get_count

print(Solution().numIslands(a))
