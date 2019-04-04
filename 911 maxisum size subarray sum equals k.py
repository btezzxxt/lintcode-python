class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        
        # add a dummy -1 bundary
        target_index_map = { k: -1 }
        
        total = 0
        maxlen = 0
        for index, num in enumerate(nums):
            total += num 
            if total in target_index_map:
                curlen = index - target_index_map[total]
                maxlen = max(maxlen, curlen)
            
            # record the first index where total + k would be target
            if total + k in target_index_map:
                continue
            else:
                target_index_map[total + k] = index
        return maxlen
        
"""
{ 
    3: -1
    4: 0,
    8: 2
    6: 3
    9: 4
}

num == 1
total = 1 
target = 1 + 3 = 4

num = -1
total = 0
target = 0 + 3 = 3

num = 5
total = 5 

num = -2 
total = 3
curlen = 4 
maxlen = 4 
target = 6 

num = 3
total = 6
curlen = 4 - 3 = 1 
maxlen = 4 
target = 9

"""
