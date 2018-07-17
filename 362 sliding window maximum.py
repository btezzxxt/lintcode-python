from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        q = deque()
        result = []
        if len(nums) < k or k == 0:
            return []

        n = len(nums)
        for i in range(n):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if i < k - 1:                        
                continue

            while len(q) and q[0] <= i - k:
                q.popleft()
            
            result.append(nums[q[0]])

        return result

print(Solution().maxSlidingWindow([1,2,7,7,8], 3))