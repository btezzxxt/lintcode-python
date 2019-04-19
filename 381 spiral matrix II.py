class Solution:
    """
    @param n: An integer
    @return: a square matrix
    """
    def generateMatrix(self, n):
        # write your code here
        # write your code here
        if n == 0:
            return []
        
        matrix = [[0] * n for i in range(n)] 
        
        cnt = 0
        m = len(matrix)
        n = len(matrix[0])
        total = n * m 

        n = n + 1
        i, j = 0, -1
        while True:
            n = n - 1
            for _ in range(n):
                cnt += 1 
                i, j = self.move(matrix, i, j, "right", cnt)
                if cnt == total:
                    return matrix
                
            m = m - 1 
            for _ in range(m):
                cnt += 1 
                i, j = self.move(matrix, i, j, "down", cnt)
                if cnt == total:
                    return matrix 
            
            n = n - 1 
            for _ in range(n):
                cnt += 1 
                i, j = self.move(matrix, i, j, "left", cnt)
                if cnt == total:
                    return matrix 
            
            m = m - 1 
            for _ in range(m):
                cnt += 1 
                i, j = self.move(matrix, i, j, "up", cnt)
                if cnt == total:
                    return matrix 
        return matrix 
        
        
    def move(self, matrix, i, j, action, count):
        if action == "right":
            j += 1 
        elif action == "down":
            i += 1 
        elif action == "left":
            j -= 1 
        elif action == "up":
            i -= 1 
            
        matrix[i][j] = count
        return i, j
            
            