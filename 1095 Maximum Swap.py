class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        # 用一个大小为10的bucket记录每个数最后出现的位置
        bucket = [-1 for i in range(10)]
        num_str = str(num)
        for index, char in enumerate(num_str):
            bucket[int(char)] = index
        
        # 从头开始遍历，第二层循环从大数开始遍历
        # 只要找到一组 在高位左边值小于右边值（high digit）就返回 
        for index, char in enumerate(num_str):
            for i in range(len(bucket) - 1, -1, -1):
                index_r = bucket[i]
                # 左边值要小， 要保证左边位数要高
                if int(char) < i and index < index_r:
                    return int(num_str[:index] + num_str[index_r] + num_str[index + 1: index_r] + num_str[index] + num_str[index_r + 1:])
        return num
            
            