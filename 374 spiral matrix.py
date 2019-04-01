class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []

        m = len(matrix)
        n = len(matrix[0])
        
        i, j = 0, -1
        res = []
        total = m * n
        
        n = n + 1
        while True:   
            n = n - 1
            if n >= 1:
                for _ in range(n):
                    i, j = self.move_and_write(i, j, matrix, res, 'right')
                    if len(res) == total:
                        return res                        
            
            m = m - 1
            if m >= 1:
                for _ in range(m):
                    i, j = self.move_and_write(i, j, matrix, res, 'down')
                    if len(res) == total:
                        return res                        

            n = n - 1
            if n >= 1:
                for _ in range(n):
                    i, j = self.move_and_write(i, j, matrix, res, 'left')
                    if len(res) == total:
                        return res                        

            m = m - 1
            if m >= 1:
                for _ in range(m):
                    i, j = self.move_and_write(i, j, matrix, res, 'up')
                    if len(res) == total:
                        return res                        
        return res


    def move_and_write(self, i, j, matrix, res, action):
        action_map = {
            "right": [0, 1],
            "down": [1, 0],
            "left": [0, -1],
            "up": [-1, 0]
        }

        i_next = i + action_map[action][0]
        j_next = j + action_map[action][1]
        res.append(matrix[i_next][j_next])
        return i_next, j_next

import itertools
counter = itertools.count(1)
a = [[next(counter) for i in range(3) ] for i in range(3)]
print(Solution().spiralOrder(a))

