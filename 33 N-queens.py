class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res = []
        visited = set()
        self.dfs([], res, visited, n)
        return self.draw(res)

    # traverse dfs
    def dfs(self, col, res, visited, n):
        if len(col) == n:
            res.append(list(col))

        for i in range(n):
            if i not in visited and self.is_valid(i, col):
                visited.add(i)
                col.append(i)
                self.dfs(col, res, visited, n)
                visited.remove(i)
                col.pop()
    
    def is_valid(self, i, col):
        nxt = len(col)
        for x, y in enumerate(col):
            if y == i:
                return False

            if x + y == nxt + i or nxt - i == x - y:
                return False
        return True


    def draw(self, res):
        results = []
        for col in res:
            n = len(col)
            graph = [['.' for i in range(n)] for j in range(n)] 
            for x, y in enumerate(col):
                graph[x][y] = 'Q'

            for i, item in enumerate(graph):
                graph[i] = ''.join(item)
            results.append(graph)
        return results

print(Solution().solveNQueens(1))

from copy import deepcopy
class Solution2:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if n == 0:
            return []
        
        board = [['.' for i in range(n)] for i in range(n)]
        
        res = []
        col = []
        self.dfs(n, col, set(), res)
        paintings = self.draw(board, res)

        return paintings 
            
            
    def dfs(self, n, col, visited, res):
        if len(col) == n:
            res.append(col[::])
            return 
        
        for i in range(n):
            if i not in visited and self.not_conflict(col, i):
                col.append(i)
                visited.add(i)
                self.dfs(n, col, visited, res)
                visited.remove(i)
                col.pop()
                
    def draw(self, board, res):
        group = []
        for col in res:
            newboard = deepcopy(board)
            for i in range(len(col)):
                newboard[i][col[i]] = 'Q'
                matrix = []
                for i in range(len(board)):
                    matrix.append("".join(newboard[i]))                
            group.append(matrix)
        return group
            
    def not_conflict(self, col, j):
        i = len(col)
        for x, y in enumerate(col):
            if x - y == i - j or x + y == i + j:
                return False
        return True
#print(Solution2().solveNQueens(3))
Solution2().not_conflict([1], 2)