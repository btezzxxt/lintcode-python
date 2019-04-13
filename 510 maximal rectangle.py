# class Solution:
#     """
#     @param matrix: a boolean 2D matrix
#     @return: an integer
#     """
#     def maximalRectangle(self, matrix):
#         # write your code here
#         def calcHeightDown(matrix):
#             m = len(matrix)
#             n = len(matrix[0])
#             for col in range(n):
#                 count = 0
#                 for i in range(m-1, -1, -1):
#                     if matrix[i][col] == 1:
#                         count += 1
#                     else:
#                         count = 0
#                     matrix[i][col] = count
        
#         def getHeight(height, index):
#             if index == -1:
#                 return 0
#             else:
#                 return height[index]

#         def calcMaxRectangleRow(height):
#             stack = [-1]
#             height.append(0)
#             s = 0
#             for i in range(len(height)):
#                 while getHeight(height, i) < getHeight(height, stack[-1]):
#                     h = getHeight(height, stack[-1])
#                     stack.pop()
#                     s = max(s, (i - stack[-1] - 1) * h)
#                 stack.append(i)
#             return s

        
#         if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
#             return 0
        
#         calcHeightDown(matrix)

#         res = 0
#         for i in range(len(matrix)):
#             area = calcMaxRectangleRow(matrix[i])
#             res = max(res, area)

#         return res

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m - 1, -1, -1):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i + 1 < m and matrix[i + 1][j] > 0:
                        matrix[i][j] = matrix[i + 1][j] + 1 
        
        maxi = 0
        for row in matrix:
            maxi = max(maxi, self.get_max_rectangle(row))
        return maxi 

    def get_max_rectangle(self, row):
        if not row:
            return 0 

        stack = [-1]
        row.append(-1)
        maxi = 0 
        for index, height in enumerate(row):
            while stack and self.get_height(row, stack[-1]) > height:
                cur_index = stack.pop()
                h = self.get_height(row, cur_index)
                left_index = stack[-1] if stack else -1
                w = index - left_index - 1 
                maxi = max(maxi, h * w)
            stack.append(index)
        return maxi

    def get_height(self, row, index):
        if index == -1:
            return 0
        else:
            return row[index]




print(Solution().maximalRectangle([[1,1,0,0,1],\
                                    [0,1,0,0,1],\
                                    [0,0,1,1,1],\
                                    [0,0,1,1,1],\
                                    [0,0,0,0,1]]))

