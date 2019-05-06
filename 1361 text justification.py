class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        # write your code here
        if not words or maxWidth == 0:
            return []
            
        line_count = 0
        lines = []
        arr = []
        
        for word in words:
            line_count = line_count + len(word) 
            if line_count > maxWidth:
                lines.append(self.format(arr, maxWidth))
                
                line_count = len(word)
                arr = [word]
            else:
                arr.append(word)
            line_count += 1 # least space between words 
        
        lines.append(self.format(arr, maxWidth))


        last_line = lines[-1]
        lines[-1] = " ".join(last_line.split())
        
        return lines
        
    def format(self, arr, maxWidth):
        count = len(arr)
        if count == 1:
            return arr[0]
        
        length = 0
        for word in arr:
            length += len(word)
            
        spaces = maxWidth - length
        least_space = spaces // (count - 1)
        
        remain = spaces - least_space * (count - 1)
        space_arr = [least_space] * (count - 1)
        for i in range(remain):
            space_arr[i] += 1 
        
        res = [] 
        for i in range(count):
            res.append(arr[i])
            if i != count - 1:
                for _ in range(space_arr[i]):
                    res.append(" ")
        return "".join(res)
        
print(Solution().fullJustify(["This","is","an","example","of","text","justification."], 16))