from collections import deque
class Solution:
    """
    @param s: The input string
    @return: Return all possible results
    """
    def removeInvalidParentheses(self, s):
        # Write your code here
        if s == "":
            return True
        
        visited = set([s])        
        queue = deque([s])
        
        res = []
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if self.is_valid(cur):
                    res.append(cur)
                
                for i in range(len(cur)):
                    if cur[i] == "(" or cur[i] == ")":
                        next_str = cur[: i] + cur[i + 1: ]
                        if next_str not in visited:
                            queue.append(next_str)
                            visited.add(next_str)
            if len(res) > 0:
                break
        return res
    
    def is_valid(self, str):
        open_p = 0 
        for char in str:
            if char == "(":
                open_p += 1 
            elif char == ")":
                open_p -= 1 
            
            if open_p < 0:
                return False 
        
        if open_p > 0:
            return False
        return True
        
            
print(Solution().removeInvalidParentheses("()())()"))