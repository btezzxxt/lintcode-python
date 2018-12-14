class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if len(nums) == 0 or len(nums) == 1:
            return

        slow = 0

        # 赋值 slow不交换， 最后补0， 可以做到写次数最少
        for fast in range(len(nums)):
            if nums[fast] != 0:
                if slow != fast:
                    nums[slow] = nums[fast]
                slow = slow + 1

        for i in range(slow, len(nums)):
            if nums[i] != 0:
                nums[i] = 0        
            # if nums[fast] != 0:
            #     nums[slow], nums[fast] = nums[fast], nums[slow]
            #     slow = slow + 1
        return
        
print(Solution().moveZeroes([0,1,0,3,12]))


