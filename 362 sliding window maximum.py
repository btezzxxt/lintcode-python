# from collections import deque
# class Solution:
#     def maxSlidingWindow(self, nums, k):
#         # write your code here
#         if len(nums) < k or k == 0:
#             return []

#         deq = deque()
#         for i in range(k):
#             while deq and deq[-1] < nums[i]:
#                 deq.pop()
#             deq.append(i)
#         res = [nums[deq[0]]]
#         for i in range(k, len(nums)):
#             if i - k == deq[0]:
#                 deq.popleft()
#             while deq and deq[-1] < nums[i]:
#                 deq.pop()
#             deq.append(i)
#             res.append(nums[deq[0]])

#         return res

# print(Solution().maxSlidingWindow([10,3], 2))

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k == 0 or not nums:
            return []

        mono_decrease_s = deque([])
        n = len(nums)
        res = []
        if n < k:
            for i in range(n):
                self.add(mono_decrease_s, nums[i])
            res.append(mono_decrease_s[0])
        else:
            for i in range(k):
                self.add(mono_decrease_s, nums[i])
            res.append(mono_decrease_s[0])
            for i in range(k, n):
                self.add(mono_decrease_s, nums[i])
                remove_val = nums[i - k]
                if remove_val == mono_decrease_s[0]:
                    mono_decrease_s.popleft()
                res.append(mono_decrease_s[0])
        return res 
    
    def add(self, stack, val):
        while stack and stack[-1] < val:
            stack.pop()
        stack.append(val)
        
print(Solution().maxSlidingWindow([10,3,4,5,1,1,2,5,5], 2))



        
        
            
    
    