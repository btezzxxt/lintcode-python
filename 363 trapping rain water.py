class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if len(heights) == 0:
            return 0
        
        l = 0
        r = len(heights) - 1
        # while l < len(heights) and heights[l] <= 0:
        #     l += 1

        # while r >= 0 and heights[r] <= 0:
        #     r -= 1

        sumVal = 0
        while l < r:
            lVal = heights[l]
            rVal = heights[r]
            if lVal < rVal:
                k = l + 1
                while k <= r and heights[k] <= lVal:
                    sumVal += lVal - heights[k]
                    k += 1
                l = k
            else:
                k = r - 1
                while k >= l and heights[k] <= rVal:
                    sumVal += rVal - heights[k]
                    k -= 1
                r = k
        return sumVal