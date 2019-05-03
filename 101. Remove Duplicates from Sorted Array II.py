class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        
        n = len(nums)
        size = 0
        count = 0
        i = 0
        while i < n:
            num = nums[i]
            # if has prev and prev == cur
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                # count++ 
                count += 1 
                # if count > 2, find the next avaliable number
                if count == 3:
                    while i < n and nums[i] == nums[i - 1]:
                        i += 1

                    # if found, resset count /  set nums[size], else continue
                    if i < n:
                        count = 1
                        nums[size] = nums[i] 
                        size += 1
                # if count <= 2, set nums[size]
                else: 
                    nums[size] = num 
                    size += 1 
            # if doesn't have prev or a new start
            else:
                # reset count / set nums[size]
                count = 1
                nums[size] = num 
                size += 1
            i += 1
        return size