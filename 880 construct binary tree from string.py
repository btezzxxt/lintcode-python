
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

import re
class Solution:
    """
    @param s: a string
    @return: a root of this tree
    """
    def str2tree(self, s):
        # write your code here
        if s == "":
            return None 
            
        op = 1 
        num = 0
        p_count = 0
        buffer = []
        child = []
        root = None

        i = 0 
        while i < len(s):
            char = s[i]
            if p_count == 0:
                if char == "-":
                    op = -1 
                elif self.is_num(char) and (i + 1 == len(s) or s[i + 1] == "("):
                    num = num * 10 + int(char)
                    num *= op 
                    root = TreeNode(num)
                elif self.is_num(char):
                    num = num * 10 + int(char)
                elif char == "(":
                    p_count += 1 
            else:
                buffer.append(char)
                if char == "(":
                    p_count += 1 
                elif char == ")":
                    p_count -= 1 
                    if p_count == 0:
                        buffer.pop()
                        child.append("".join(buffer))
                        buffer = []
            i += 1 
        if len(child) > 0:
            root.left = self.str2tree(child[0])
        
        if len(child) > 1:
            root.right = self.str2tree(child[1])
        return root 
                
                
    def is_num(self, char):
        return re.match(r"[0-9]", char)