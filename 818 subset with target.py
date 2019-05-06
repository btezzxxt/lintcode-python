# class Solution:
#     """
#     @param nums: the array
#     @param target: the target
#     @return: the number of subsets which meet the following conditions
#     """
#     def subsetWithTarget(self, nums, target):
#         # Write you code here
#         nums.sort()
#         ans = 0
#         for i in range(0, len(nums)):
#             j = i
#             while(j + 1 < len(nums) and nums[i] + nums[j+1] < target):
#                 j += 1
#             if (nums[i] + nums[j] < target):
#                 ans = ans + (1<<(j - i))
#         return ans

class Solution:
    """
    @param nums: the array
    @param target: the target
    @return: the number of subsets which meet the following conditions
    """
    def subsetWithTarget(self, nums, target):
        # Write you code here
        nums.sort()
        total = 0
        for i in range(len(nums)):
            end = i
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    end = j    
                    continue
                else:
                    break
            if nums[i] + nums[end] < target:
                total += pow(2, end - i)
        return total
print(Solution().subsetWithTarget([1,2,3,4,5], 5))