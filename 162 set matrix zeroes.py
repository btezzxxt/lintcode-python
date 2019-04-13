# class Solution:
#     """
#     @param matrix: A lsit of lists of integers
#     @return: nothing
#     """
#     def setZeroes(self, matrix):
        # write your code here
        # if not matrix or not matrix[0]:
        #     return
        
        # m = len(matrix)
        # n = len(matrix[0])

        # col = set()
        # row = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row.add(i)
        #             col.add(j)

        # for i in row:
        #     for j in range(n):
        #         matrix[i][j] = 0 
        
        # for j in col:
        #     for i in range(m):
        #         matrix[i][j] = 0

class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def get_first_zero_idx(self, matrix):   
        col, row = -1, -1
        m = len(matrix)
        n = len(matrix[0])        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col, row = i, j 
                    return col, row
        return -1, -1 

    def setZeroes(self, matrix):
        if not matrix or not matrix[0]:
            return 
        
        m = len(matrix)
        n = len(matrix[0])

        # 1. find first zero position, use that row to record column zeros, use that column to record row zeroes
        row_records_col, col_records_row = self.get_first_zero_idx(matrix)
        if row_records_col == -1:
            return 

        # 2. record all the zero row/cols
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[row_records_col][j] = 0
                    matrix[i][col_records_row] = 0 

        # 3. mark columns to zeros base on row_records_col
        for i in range(n):
            if matrix[row_records_col][i] == 0:
                target_col = i 
                # attention: skip the column for recording 
                if target_col != col_records_row:
                    for j in range(m):
                        matrix[j][target_col] = 0
        
        for i in range(m):
            if matrix[i][col_records_row] == 0:
                target_row = i
                if target_row != row_records_col:
                    # skip the row for recording
                    for j in range(n):
                        matrix[target_row][j] = 0
        
        # 4. mark two recorders to be zeroes
        for i in range(n):
            matrix[row_records_col][i] = 0

        for i in range(m):
            matrix[i][col_records_row] = 0


print(Solution().setZeroes([[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]))