from heapq import heappop, heappush

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        dx = [0,1]
        dy = [1,0]
        hash = {}
        n = len(matrix)
        m = len(matrix[0])
        heap = [(matrix[0][0], (0, 0))]

        for i in range(1, k):
            (val, cor) = heappop(heap)
            for j in range(2):
                nextx = cor[0] + dx[j]
                nexty = cor[1] + dy[j]
                nextid = nextx * m + nexty
                if nextx < n and nexty < m and not nextid in hash:
                    hash[nextid] = True
                    nextval = matrix[nextx][nexty]
                    heappush(heap, (nextval, (nextx, nexty)))
        return heappop(heap)[0]

print(Solution().kthSmallest([[1,5,7],[3,7,8],[4,8,9]],4))
                
# import heapq
# class Solution:
#     """
#     @param matrix: a matrix of integers
#     @param k: An integer
#     @return: the kth smallest number in the matrix
#     """
#     def kthSmallest(self, matrix, k):
#         # write your code here
#         n = len(matrix)
#         m = len(matrix[0])
#         heap = []
#         heapq.heapify(heap)
        
#         for j in range(m):
#             for i in range(n):
#                 heapq.heappush(heap, matrix[i][j])

#         while k > 1:
#             k -= 1
#             heapq.heappop(heap)
#         return heapq.heappop(heap)
                


