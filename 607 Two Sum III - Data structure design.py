# class TwoSum:
#     """
#     @param number: An integer
#     @return: nothing
#     """
#     added = {}
#     existSum = {}

#     O(n2) space O(n) time
#     def add(self, number):
#         # write your code here

#         if number not in self.added and len(self.added.keys()) > 0:
#             for key in self.added.keys():
#                 sum = key + number
#                 if sum not in self.existSum:
#                     self.existSum[sum] = True

#         elif number in self.added and self.added[number] == 1:
#             self.existSum[number + number] = True

#         if number not in self.added:
#             self.added[number] = 1
#         else:
#             self.added[number] = self.added[number] + 1
        

#     """
#     @param value: An integer
#     @return: Find if there exists any pair of numbers which sum is equal to the value.
#     """
#     O(1) time
#     def find(self, value):
#         # write your code here
#         return value in self.existSum

class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    added = []

    def add(self, number):
        # write your code here
        self.added.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # 双指针夹逼典型
        self.added.sort() # O(nlogn)
        left = 0
        right = len(self.added) - 1
        while left < right:
            sum = self.added[left] + self.added[right]
            if sum == value:
                return True
            elif sum > value:
                right = right - 1
            else:
                left = left + 1
        return False

        
