# class Solution:
#     """
#     @param board: A list of lists of character
#     @param word: A string
#     @return: A boolean
#     """
#     def exist(self, board, word):
#         # write your code here
#         if len(board) == 0 or len(board[0]) == 0:
#             return False
        
#         if len(word) == 0:
#             return True
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     found = self.dfsFind(board, i, j, word, 0)
#                     if found:
#                         return True
        
#         return False
    
#     def dfsFind(self, board, i, j, word, start):
#         if start == len(word):
#             return True
        
#         if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[start] != board[i][j]:
#             return False
        
#         # mark i j as visited or we could use extra O(mn) space to mark visited
#         board[i][j] = '#'

#         dx = [-1, 1, 0, 0]
#         dy = [0, 0, -1, 1]

#         for k in range(4):
#             new_i = i + dx[k]
#             new_j = j + dy[k]
#             found = self.dfsFind(board, new_i, new_j, word, start + 1)
#             if found:
#                 board[i][j] = word[start]
#                 return True
#         board[i][j] = word[start]
#         return False

    # def dfsFind(self, board, i, j, word, start):
    #     if start == len(word):
    #         return True
        
    #     if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[start] != board[i][j]:
    #         return False
        
    #     # mark i j as visited or we could use extra O(mn) space to mark visited
    #     board[i][j] = '#'
    #     found = self.dfsFind(board, i - 1, j, word, start + 1) 
    #     if not found:
    #         found2 = self.dfsFind(board, i + 1, j, word, start + 1) 
    #         if not found2:
    #             found3 = self.dfsFind(board, i, j - 1, word, start + 1) 
    #             if not found3:
    #                 found4 = self.dfsFind(board, i, j + 1, word, start + 1)

    #     board[i][j] = word[start]

    #     return found or found2 or found3 or found4
                
class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not board or not board[0]:
            return False 
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, 1, word, set([(i, j)])):
                        return True 

        return False

    def dfs(self, board, i, j, index, word, visited):
        if len(word) == index:
            return True 

        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for k in range(4):
            di = dx[k] + i 
            dj = dy[k] + j 
        
            if di >= 0 and di < len(board) and dj >= 0 and dj < len(board[0]) and (di, dj) not in visited and board[di][dj] == word[index]:
                visited.add((di, dj))
                if self.dfs(board, di, dj, index + 1, word, visited):
                    return True 
        
                visited.remove((di, dj))
        return False


print(Solution().exist(["b","a", "b", "b", "a"], "baa"))