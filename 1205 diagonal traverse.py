import collections
class Solution:
    """
    @param matrix: a 2D array
    @return: return a list of integers
    """
    def findDiagonalOrder(self, matrix):
        # write your code here
        diagonals = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diagonals[i + j].append(matrix[i][j])

        res = [] 
        for id, arr in diagonals.items():
            if id % 2 == 0:
                arr.reverse()
            res.extend(arr)
        return res 
    
matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

print(Solution().findDiagonalOrder(matrix))