class Solution:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        
        left_product_i = []
        prod = 1 
        for i in range(n):
            prod = prod * nums[i]
            left_product_i.append(prod)
        
        prod = 1 
        right_product_i = []
        for i in range(n - 1, -1, -1):
            prod *= nums[i]
            right_product_i.append(prod)
        right_product_i.reverse()
        
        res = []
        for i in range(n):
            left = left_product_i[i - 1] if i - 1 >= 0 else 1 
            right = right_product_i[i + 1] if i + 1 < n else 1 
            res.append(left * right)
            
        return res