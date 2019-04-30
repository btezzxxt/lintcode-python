class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """
    def candyCrush(self, board):
        # Write your code here
        if not board or not board[0]:
            return board 
            
        m = len(board)
        n = len(board[0])
        
        to_del_pos = [[0 for i in range(n)] for i in range(m)]
        
        has_crush = self.mark_for_del(to_del_pos, board)
        while has_crush:
            self.delete_and_fill(to_del_pos, board)
            has_crush = self.mark_for_del(to_del_pos, board)
        
        return board 
    
    def delete_and_fill(self, to_del_pos, board):
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if to_del_pos[i][j] == 1:
                    board[i][j] = 0
        
        for j in range(n):
            p1 = m - 1 
            p2 = m - 1 
            while p2 >= 0:
                if board[p2][j] != 0:
                    board[p2][j], board[p1][j] = board[p1][j], board[p2][j]
                    p1 -= 1 
                    p2 -= 1 
                else:
                    p2 -= 1 
    
    def mark_for_del(self, to_del_pos, board):
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                to_del_pos[i][j] = 0
        
        has_crush = False
        
        for i in range(m):
            k = 0
            j = 0
            
            while j <= n:
                if j != n and board[i][k] == board[i][j]:
                    j += 1 
                else:
                    if j - k >= 3:
                        while k < j:
                            if board[i][k] != 0:
                                to_del_pos[i][k] = 1
                                has_crush = True
                            k += 1
                    else:
                        k = j 
                        j += 1

        for j in range(n):
            k = 0
            i = 0
            while i <= m:
                if i != m and board[k][j] == board[i][j]:
                    i += 1 
                else:
                    if i - k >= 3:
                        while k < i:
                            if board[k][j] != 0:
                                to_del_pos[k][j] = 1
                                has_crush = True
                            k += 1 
                    else:
                        k = i 
                        i += 1
              
        return has_crush
                            
print(Solution().candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))                
                            