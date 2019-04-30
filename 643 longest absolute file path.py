class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        # write your code here
        if not input:
            return 0
        
        lines = input.split('\n')
        level = 0
        
        sum_at_level = [0] * len(input)
        max_length = 0
        
        for line in lines:
            count = line.count('\t')
            if count == 0:
                sum_at_level[0] = len(line)
            else:
                sum_at_level[count] = sum_at_level[count - 1] + len(line) - count 
            
            if line.find('.') != -1:
                max_length = max(max_length, sum_at_level[count] + count)
        return max_length