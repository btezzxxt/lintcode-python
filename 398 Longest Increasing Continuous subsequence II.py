import sys
class Solution:
    """
    @param A: An integer matrix
    @return: an integer
    """
    def longestIncreasingContinuousSubsequenceII(self, A):
        # write your code here
        if len(A) == 0 or len(A[0]) == 0:
            return 0
        
        m = len(A)
        n = len(A[0])

        visited = [[0] * n for i in range(m)]

        F = [[1] * n for i in range(m)]

        max_ = -sys.maxsize
        for i in range(m):
            for j in range(n):
                max_ = max(max_, self.search(i, j, A, visited, F))
        return max_

    def search(self, i, j, A, visited, F):
        if visited[i][j] == 1:
            return F[i][j]

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for k in range(4):
            iNew = i + dx[k]
            jNew = j + dy[k]

            if 0 <= iNew and iNew < len(A) and 0 <= jNew and jNew < len(A[0]):
                if A[i][j] > A[iNew][jNew]:
                    F[i][j] = max(F[i][j], self.search(iNew, jNew, A, visited, F) + 1)

        
        visited[i][j] = 1
        return F[i][j]


print(Solution().longestIncreasingContinuousSubsequenceII([[1,2,3,4,5],[16,17,24,23,6],[15,18,25,22,7],[14,19,20,21,8],[13,12,11,10,9]]))
                
            