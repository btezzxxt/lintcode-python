class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        # write your code here
        def getHeight(height, index):
            if index != -1:
                return height[index]
            else:
                return 0

        if len(height) == 0:
            return 0

        stack = [-1]
        height.append(0)

        area = 0
        for i in range(len(height)):
            while getHeight(height, i) < getHeight(height, stack[-1]):
                curHeight = getHeight(height, stack[-1])
                stack.pop()
                area = max(area, (i - stack[-1] - 1) * curHeight)
            stack.append(i)
        return area
        
print(Solution().largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))
        