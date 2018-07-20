from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if len(nums) < k or k == 0:
            return []

        deq = deque()
        for i in range(k):
            while deq and deq[-1] < nums[i]:
                deq.pop()
            deq.append(i)
        res = [nums[deq[0]]]
        for i in range(k, len(nums)):
            if i - k == deq[0]:
                deq.popleft()
            while deq and deq[-1] < nums[i]:
                deq.pop()
            deq.append(i)
            res.append(nums[deq[0]])

        return res

print(Solution().maxSlidingWindow([10,3], 2))

