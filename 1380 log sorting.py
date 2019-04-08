import re
class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        c1 = []
        c2 = []
        for log in logs:
            index = log.find(" ")
            content = log[index + 1:]
            id = log[: index + 1]
            
            if self.alphaonly(content):
                c1.append((content, id))
            else:
                c2.append(log)
        
        c1.sort()
        res = []
        for content, id in c1:
            res.append(id + content)
        res.extend(c2)
        return res 
    
    def alphaonly(self, string):
        return re.match(r"^[a-zA-Z ]+$", string)