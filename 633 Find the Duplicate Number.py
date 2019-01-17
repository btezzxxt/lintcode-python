class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    # slow/fast pointer
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = nums[slow]
        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    # binary search
    # def findDuplicate(self, nums):
    #     # write your code here
    #     start, end = 1, len(nums) - 1
    #     while start + 1 < end:
    #         mid = (start + end) // 2
    #         if self.smaller_than_or_equal_to(nums, mid) > mid:
    #             end = mid
    #         else:
    #             start = mid
        
    #     if self.smaller_than_or_equal_to(nums, start) > start:
    #         return start
    #     return end
    
    # def smaller_than_or_equal_to(self, nums, val):
    #     count = 0
    #     for num in nums:
    #         if num <= val:
    #             count += 1
    #     return count
print(Solution().findDuplicate([1,1,1,1]))