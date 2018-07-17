class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        def calcHeightDown(matrix):
            m = len(matrix)
            n = len(matrix[0])
            for col in range(n):
                count = 0
                for i in range(m-1, -1, -1):
                    if matrix[i][col] == 1:
                        count += 1
                    else:
                        count = 0
                    matrix[i][col] = count
        
        def getHeight(height, index):
            if index == -1:
                return 0
            else:
                return height[index]

        def calcMaxRectangleRow(height):
            stack = [-1]
            height.append(0)
            s = 0
            for i in range(len(height)):
                while getHeight(height, i) < getHeight(height, stack[-1]):
                    h = getHeight(height, stack[-1])
                    stack.pop()
                    s = max(s, (i - stack[-1] - 1) * h)
                stack.append(i)
            return s

        
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        calcHeightDown(matrix)

        res = 0
        for i in range(len(matrix)):
            area = calcMaxRectangleRow(matrix[i])
            res = max(res, area)

        return res

print(Solution().maximalRectangle([[1,1,0,0,1],[0,1,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,1]]))

