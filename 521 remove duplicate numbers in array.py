class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        #O(n) space / time
        # map = {}
        # slow = 0 
        # for fast in range(len(nums)):
        #     if nums[fast] not in map:
        #         nums[slow] = nums[fast]
        #         map[nums[slow]] = True
        #         slow = slow + 1
        # return slow


        # sort O(nlogn)
        nums.sort()
        slow = 1

        # 模板， 快指针处理
        for fast in range(1, len(nums)):
            # if fast condition，在move zeroes是第一个非零，这题是第一个变化数字，然后赋值慢指针，慢指针+1
            if (nums[fast] != nums[fast - 1]):
                nums[slow] = nums[fast]
                slow = slow + 1
        # index + 1 is just the number
        return slow


print(Solution().deduplication([1,3,1,4,4,2]))
