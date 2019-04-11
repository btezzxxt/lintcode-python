# class Solution:
#     """
#     @param height: A list of integer
#     @return: The area of largest rectangle in the histogram
#     """
#     def largestRectangleArea(self, height):
#         # write your code here
#         def getHeight(height, index):
#             if index != -1:
#                 return height[index]
#             else:
#                 return 0

#         if len(height) == 0:
#             return 0

#         stack = [-1]
#         height.append(0)

#         area = 0
#         for i in range(len(height)):
#             while getHeight(height, i) < getHeight(height, stack[-1]):
#                 curHeight = getHeight(height, stack[-1])
#                 stack.pop()
#                 area = max(area, (i - stack[-1] - 1) * curHeight)
#             stack.append(i)
#         return area
        
# print(Solution().largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))


class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        if not height:
            return 0 
        
        stack = [(0, -1)]
        max_area = -1
        height.append(-1)
        for index, h in enumerate(height):
            if not stack:
                stack.append((h, index))
            else:
                if h >= stack[-1][0]:
                    stack.append((h, index))
                else:
                    top = None
                    while stack and stack[-1][0] > h:
                        top = stack.pop()
                        area = top[0] * (index - top[1])
                        max_area = max(area, max_area)
                    if top:
                        stack.append(((h, top[1])))
                    else:
                        stack.append((h, index))
        return max_area

print(Solution().largestRectangleArea([2,1,5,6,2,3]))