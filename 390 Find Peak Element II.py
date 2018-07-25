class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return [-1, -1]
        
        top = 0
        bot = len(A) - 1
        left = 0
        right = len(A[0]) - 1

        while left + 1 < right or top + 1 < bot:
            if bot - top > right - left:
                r = top + (bot - top) // 2
                c = self.maxInRow(A, r, left, right)
                if A[r + 1][c] > A[r][c]:
                    top = r
                else:
                    bot = r
            else:
                c = left + (right - left) // 2
                r = self.maxInCol(A, c, top, bot)
                if A[r][c+1] > A[r][c]:
                    left = c
                else:
                    right = c
        
        for r in [top, bot]:
            for c in [left, right]:
                if self.isPeak(A, r, c):
                    return [r, c]
        
        return [-1, -1]
    
    def maxInRow(self, A, r, start, end):
        max_ = A[r][start]
        idx = start
        for i in range(start, end + 1):
            if A[r][i] > max_:
                max_ = A[r][i]
                idx = i
        return idx

    def maxInCol(self, A, c, start, end):
        max_ = A[start][c]
        idx = start
        for i in range(start, end + 1):
            if A[i][c] > max_:
                max_ = A[i][c]
                idx = i
        return idx

    def isPeak(self, A, r, c):
        m = len(A)
        n = len(A[0])
        if not self.validIdx(r, c, m, n):
            return False
        
        up = -1 if not self.validIdx(r+1, c, m, n) else A[r+1][c]
        down = -1 if not self.validIdx(r-1, c, m, n) else A[r-1][c]
        l = -1 if not self.validIdx(r, c+1, m, n) else A[r][c+1]
        right = -1 if not self.validIdx(r, c-1, m, n) else A[r][c-1]

        return A[r][c] >= max(up, down, l, right)


    def validIdx(self, r, c, m, n):
        if 0 <= r and r < m and 0 <= c and c < n:
            return True
        return False
        







print(Solution().findPeakII([[1,2,3,4,5,6],[14,15,16,17,18,8],[12,13,11,10,9,7]]))


# class Solution:
#     #@param A: An list of list integer 
#     #@return: The index of position is a list of integer, for example [2,2]
#     def findPeakII(self, A):
#         if len(A) == 0 or len(A[0]) == 0:
#             return [-1, -1]
            
#         left, up = 0, 0
#         right, down = len(A[0]) - 1, len(A) - 1
#         while left + 1  < right or up + 1 < down:
#             if right - left > down - up:
#                 c = (left + right) // 2
#                 r = self.findColumnPeak(A, c, up, down)
#                 if A[r][c] < A[r][c - 1]:
#                     right = c
#                 else:
#                     left = c
#             else:
#                 r = (up + down) // 2
#                 c = self.findRowPeak(A, r, left, right)
#                 if A[r][c] < A[r - 1][c]:
#                     down = r
#                 else:
#                     up = r
        
#         for c in [left, right]:
#             for r in [up, down]:
#                 if self.isPeak(A, r, c):
#                     return [r, c]
#         return [-1, -1]
        
#     def isPeak(self, A, r, c):
#         a, b, x, y = -1, -1, -1, -1
#         m = len(A)
#         n = len(A[0])

#         if not (0 <= r and r < m and 0 <= c  and c < n):
#             return False
            
#         if 0 <= r and r < m and 0 <= c - 1 and c-1 < n:
#             a = A[r][c-1] 
            
#         if 0 <= r and r < m and 0 <= c + 1 and c+1 < n:
#             b = A[r][c+1]

#         if 0 <= r - 1 and r - 1 < m and 0 <= c and c < n:
#             x = A[r-1][c]

#         if 0 <= r + 1 and r + 1 < m and 0 <= c and c < n:
#             y = A[r+1][c] 
        
#         return A[r][c] > max(a, b, x, y)
    
#     def findColumnPeak(self, A, c, up, down):
#         mv = A[up][c]
#         idx = up
#         for r in range(up+1, down + 1):
#             if A[r][c] > mv:
#                 mv = A[r][c]
#                 idx = r
#         return idx

    
#     def findRowPeak(self, A, r, left, right):
#         mv = A[r][left]
#         idx = left
#         for c in range(left+1, right + 1):
#             if A[r][c] > mv:
#                 mv = A[r][c]
#                 idx = c
#         return idx        
