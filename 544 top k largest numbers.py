# from heapq import heappop, heappush
# class Solution:
#     """
#     @param nums: an integer array
#     @param k: An integer
#     @return: the top k largest numbers in array
#     """
#     def topk(self, nums, k):
#         # write your code here
#         heap = []
#         for num in nums:
#             heappush(heap, -num)
        
#         res = []
#         for _ in range(k):
#             res.append(-heappop(heap))

#         return res

from heapq import heappop, heappush
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here

        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                heappush(heap, num)
                heappop(heap)

        res = []
        while k > 0:
            res.append(heappop(heap))
            k -= 1
        res.reverse()            
        return res

print(Solution().topk([5,3,2,1,4], 3))