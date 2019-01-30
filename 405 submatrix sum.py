class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return []  
        
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(0, m):
            arr = [0 for _ in range(n)]
            for j in range(i, m):
                for k in range(n):
                    arr[k] += matrix[j][k]
                location = self.subSum(arr)
                if location:
                    return [(i, location[0]), (j, location[1])]

        return []

    # 一个dict保存前缀和
    def subSum(self, arr):
        # sum: index
        # 这个初始化非常关键，要不然无法处理全部加起来为零的情况
        prefixsum = {0: -1}
        total = 0
        for i, value in enumerate(arr):
            total += value
            if total in prefixsum:
                return (prefixsum[total] + 1, i)
            prefixsum[total] = i
        return None
        
        
print(Solution().submatrixSum([[2,-2],[-4,4]]))