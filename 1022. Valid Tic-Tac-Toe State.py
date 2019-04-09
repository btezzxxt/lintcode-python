class Solution:
    """
    @param board: the given board
    @return: True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game
    """
    def validTicTacToe(self, board):
        # Write your code
        num_x = self.count_x(board)
        num_o = self.count_o(board)
        
        if self.x_won(board):
            if num_x - num_o == 1:             
                return True 
            else:
                return False
        
        elif self.o_won(board):
            if num_x == num_o:
                return True 
            else:
                return False
        else:
            # nobody won yet, we could have two states
            if num_x == num_o or num_x - num_o == 1:
                return True
            
        return False
        
    def count_x(self, board):
        total = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    total += 1     
        return total 
                    
    def count_o(self, board):
        total = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    total += 1          
        return total 
    
    def x_won(self, board):
        arr = []
        for line in board:
            arr.extend(list(line))
            
        wins = [[0,4,8], [2,4,6], [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
        for a, b, c in wins:
            if arr[a] == "X" and arr[a] == arr[b] and arr[b] == arr[c]:
                return True 
        return False
        
    def o_won(self, board):
        arr = []
        for line in board:
            arr.extend(list(line))
            
        wins = [[0,4,8], [2,4,6], [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8]]
        for a, b, c in wins:
            if arr[a] == "O" and arr[a] == arr[b] and arr[b] == arr[c]:
                return True 
        return False        
                

            
            
            
            
            
            
        
        
        