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