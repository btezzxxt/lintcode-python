import sys
class Solution:
    """
    @param matrix: the given matrix
    @return: the largest possible sum
    """
    # 降维 2d变成1d 使用前缀和，枚举每一个纵向上从i到j（m以内）的矩阵，纵向上求和变成一维数组
    def maxSubmatrix(self, matrix):
        # write your code here
        if not matrix:
            return 0
        
        if not matrix[0]:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])

        array = []
        res = -sys.maxsize

        for i in range(m):
            array = list(matrix[i])
            for j in range(i, m):
                if j != i:
                    for k in range(m):
                        array[k] += matrix[j][k]
                max_value = self.maxSubarryValue(array)
                res = max(res, max_value)
        return res

    def maxSubarryValue(self, array):
        sum = 0 
        max_gap = -sys.maxsize
        min_sum = 0

        for num in array:
            sum += num
            max_gap = max(max_gap, sum - min_sum)
            min_sum = min(sum, min_sum)

        return max_gap
        