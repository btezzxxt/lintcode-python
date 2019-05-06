class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        hashmap_total_index = {0: -1}
        
        total = 0
        maxlen = 0
        for index, num in enumerate(nums):
            val = -1 if num == 0 else 1 
            total += val 
            if total in hashmap_total_index:
                maxlen = max(maxlen, index - hashmap_total_index[total])
            else:
                hashmap_total_index[total] = index 
        return maxlen