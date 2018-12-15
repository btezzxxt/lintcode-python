class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        res_map = {} # might take extra space but py can use turple as map key
        for i in range(len(numbers)-2):
            # use a map or if i > 0 and numbers[i] == nums[i - 1]: continue
            l = i + 1
            r = len(numbers) - 1
            target = -numbers[i]
            while l < r:
                if numbers[l] + numbers[r] == target:
                    temp = (numbers[i], numbers[l], numbers[r])
                    if temp not in res_map:
                        res.append(temp)
                        res_map[temp] = True
                    l = l + 1 
                    r = r - 1
                elif numbers[l] + numbers[r] < target:
                    l = l + 1
                else:
                    r = r - 1
        return res
