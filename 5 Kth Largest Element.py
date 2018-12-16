class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # kth biggest is len(nums) - k index smallest
        smallest = len(nums) - n
        return self.partition(nums, 0, len(nums) - 1, smallest)
    # get kth smallest
    def partition(self, nums, start, end, k):
        if start == end:
            return nums[k]
        
        l, r = start, end

        pivot = nums[(l + r)//2] 
        while l <= r:
            while l <= r and nums[r] > pivot:
                r = r - 1
            while l <= r and nums[l] < pivot:
                l = l + 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l = l + 1 
                r = r - 1
        
        if k >= l:
            return self.partition(nums, l, end, k)
        elif k <= r:
            return self.partition(nums, start, r, k) 
        return nums[k]