class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        horiz_points = self.get_horiz(A)
        verti_points = self.get_vertical(B)

        max_col = 0
        max_row = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                total = 0
                if i in horiz_points and j in verti_points:
                    row = horiz_points[i]
                    col = verti_points[j]
                    total = 0
                    for row_col in row:
                        if row_col in col:
                            max_col = max(max_col, j)
                            max_row = max(max_row, i)

        C = [[0 for i in range(max_col + 1)] for i in range(max_row + 1)]
        for i in range(len(C)):
            for j in range(len(C[0])):
                total = 0
                if i in horiz_points and j in verti_points:
                    row = horiz_points[i]
                    col = verti_points[j]
                    total = 0
                    for row_col in row:
                        if row_col in col:
                            total += A[i][row_col] * B[row_col][j]
                C[i][j] = total
        return C
    
    def get_horiz(self, A):
        res = {}
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    if i in res:
                        res[i].add(j)
                    else:
                        res[i] = set([j])
        return res


    def get_vertical(self, B):
        res = {}
        for i in range(len(B[0])):
            for j in range(len(B)):
                if B[j][i] != 0:
                    if i in res:
                        res[i].add(j)
                    else:
                        res[i] = set([j])
        return res

A = [[7,0,0],[1,0,3]]
B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(Solution().multiply(A, B))