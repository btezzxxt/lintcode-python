class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        if len(str) == 0:
            return str
            
        start = 0
        end = 0
        str_arr = list(str)
        self.reverse(str_arr, 0, len(str_arr) - 1)
        for char in str_arr:
            if char == " ":
                self.reverse(str_arr, start, end - 1)
                start = end + 1 
            end += 1
            
        self.reverse(str_arr, start, end - 1)
        return "".join(str_arr)
        
    def reverse(self, arr, start, end):
        if start >= end:
            return 
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1 
            end -= 1 
            
        