class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        target_map = {}
        for idx, number in enumerate(numbers):
            if number not in target_map:
                target_map[target - number] = idx
            else:
                return [target_map[number], idx]
    