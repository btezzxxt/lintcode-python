class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    total = 0
    def totalNQueens(self, n):
        # write your code here
        self.dfs([], set(), n)
        return self.total

    def dfs(self, col, visited, n):
        if len(col) == n:
            self.total += 1
            return
        
        for i in range(n):
            if i not in visited and self.is_valid(col, i):
                col.append(i)
                visited.add(i)
                self.dfs(col, visited, n)
                col.pop()
                visited.remove(i)
    
    def is_valid(self, col, i):
        for index, c in enumerate(col):
            if c == i:
                return False
            
            if index + c == len(col) + i or index - c == len(col) - i:
                return False
        return True

print(Solution().totalNQueens(1))