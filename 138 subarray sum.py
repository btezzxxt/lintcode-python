class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        sum_map = {0: -1}
        total = 0

        for i, num in enumerate(nums):
            total += num
            if total in sum_map:
                return [sum_map[total] + 1, i]
            sum_map[total] = i
        return []
            
print(Solution().subarraySum([-3,1,2,-3,4]))


class Solution2:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        sum_hash = { 0: -1 }
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total in sum_hash:
                return [sum_hash[total] + 1, i]
            else:
                sum_hash[total] = i
        return []        