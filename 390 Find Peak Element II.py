class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]

# will rewrite tomorrow

    def findPeakII(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]
            
        left, up = 0, 0
        right, down = len(A[0]) - 1, len(A) - 1
        while left + 1  < right or up + 1 < down:
            if right - left > down - up:
                c = (left + right) // 2
                r = self.findColumnPeak(A, c, up, down)
                if A[r][c] < A[r][c - 1]:
                    right = c
                else:
                    left = c
            else:
                r = (up + down) // 2
                c = self.findRowPeak(A, r, left, right)
                if A[r][c] < A[r - 1][c]:
                    down = r
                else:
                    up = r
        
        for c in [left, right]:
            for r in [up, down]:
                if self.isPeak(A, r, c):
                    return [r, c]
        return [-1, -1]
        
    def isPeak(self, A, r, c):
        a, b, x, y = -1, -1, -1, -1
        m = len(A)
        n = len(A[0])

        if not (0 <= r and r < m and 0 <= c  and c < n):
            return False
            
        if 0 <= r and r < m and 0 <= c - 1 and c-1 < n:
            a = A[r][c-1] 
            
        if 0 <= r and r < m and 0 <= c + 1 and c+1 < n:
            b = A[r][c+1]

        if 0 <= r - 1 and r - 1 < m and 0 <= c and c < n:
            x = A[r-1][c]

        if 0 <= r + 1 and r + 1 < m and 0 <= c and c < n:
            y = A[r+1][c] 
        
        return A[r][c] > max(a, b, x, y)
    
    def findColumnPeak(self, A, c, up, down):
        mv = A[up][c]
        idx = up
        for r in range(up+1, down + 1):
            if A[r][c] > mv:
                mv = A[r][c]
                idx = r
        return idx

    
    def findRowPeak(self, A, r, left, right):
        mv = A[r][left]
        idx = left
        for c in range(left+1, right + 1):
            if A[r][c] > mv:
                mv = A[r][c]
                idx = c
        return idx        


print(Solution().findPeakII([[1,2,3,4,5,6],[14,15,16,17,18,8],[12,13,11,10,9,7]]))