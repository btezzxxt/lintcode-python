# 这是找带重复的版本
class Solution:
    """
    @param matrix: an integer matrix
    @return: the length of the longest increasing path
    """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]    
    def longestIncreasingPath(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0 
            
        memo = {}
        local_max = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                next_max = self.dfs(matrix, i, j, memo, set([(i, j)]))
                local_max = max(local_max, next_max)
        return local_max
        
    def dfs(self, matrix, i, j, memo, visited_this_round):
        if (i, j) in memo:
            return memo[(i, j)]
     
        local_max = 1
        for k in range(4):
            di = i + self.dx[k]
            dj = j + self.dy[k]
            if di >= 0 and di < len(matrix) and dj >= 0 and dj < len(matrix[0]) and matrix[di][dj] <= matrix[i][j] and (di, dj) not in visited_this_round:
                visited_this_round.add((di, dj))
                next_max = self.dfs(matrix, di, dj, memo, visited_this_round)                
                local_max = max(local_max, next_max + 1)
        memo[(i, j)] = local_max
        return local_max
                
        
        
                
print(Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))