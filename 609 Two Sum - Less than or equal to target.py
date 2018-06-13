# class Solution:
#     """
#     @param nums: an array of integer
#     @param target: an integer
#     @return: an integer
#     """
#     def twoSum5(self, nums, target):
#         # write your code here
#         def bs_get_max_i_eq_k(nums, k):
#             l = 0
#             r = len(nums) - 1
#             while l < r:
#                 m = l + (r - l + 1)//2
#                 if nums[m] > k:
#                     r = m - 1
#                 else:
#                     l = m
#             if (nums[l] == k):
#                 return l
#             return -1
        
#         def bs_get_max_i_lt_k(nums, k):
#             l = 0
#             r = len(nums) - 1
#             while l < r:
#                 m = l + (r - l + 1)//2
#                 if nums[m] >= k:
#                     r = m - 1
#                 else:
#                     l = m
#             if (nums[l] < k):
#                 return l
#             return -1
        
#         count = 0
#         for i, val in enumerate(nums):
#             left = target - val
#             index = bs_get_max_i_eq_k(nums, left)
#             if index == -1:
#                 index = bs_get_max_i_lt_k(nums, left)
#                 if index == -1:
#                     continue
#             if index >= i:
#                 count += index + 1 - 1
#             else:
#                 count += index + 1
#         return count // 2
        
# print(Solution().twoSum5([-1, 0 , 1], 0)) 
# O(nlog(n)) logn for binary search 
# end

# O(n)
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        l = 0
        r = len(nums) - 1
        nums.sort()
        count = 0
        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            else:
                count += l - r
                l += 1
        return count

print(Solution().twoSum5([2, 3 , 5, 7], 7)) 


