from heapq import heappush, heappop
class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        if k == 0:
            return 0

        len1 = len(A)
        len2 = len(B)

        if len1 == 0 or len2 == 0:
            return 0

        dx = [0,1]        
        dy = [1,0]

        dic = {}

        minheap = []
        heappush(minheap, (A[0] + B[0], (0, 0)))
        
        i = 0
        while i < k-1:
            cur_pair = heappop(minheap)[1]
            for j in range(2):
                next_A_index = cur_pair[0] + dx[j]
                next_B_index = cur_pair[1] + dy[j]
                if next_A_index < len1 and next_B_index < len2 and not (next_A_index, next_B_index) in dic:
                    heappush(minheap, (A[next_A_index]+B[next_B_index], (next_A_index, next_B_index)))
            i += 1

        return minheap[0][0]
