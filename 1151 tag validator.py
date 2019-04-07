import re
class Solution:
    """
    @param code: the given code
    @return: whether it is valid
    """
    def isValid(self, code):
        # Write your code here
        if len(code) == 0:
            return False
        
        if code[0] != "<":
            return False
            
        stack = []     
        i = 0       
        while i < len(code):
            # 对于cdata来说 只要能找到开口闭口就是valid
            if code[i: i + 9] == "<![CDATA[":
                index = code.find("]]>", i + 9)
                if index == -1:
                    return False
                i = index + 3 
            # 对于close tag来说 需要1. 能找到闭口 2.tagname要能match stack中的上一个 3.出栈
            elif code[i : i + 2] == "</":
                index = code.find(">", i + 2)
                if index == -1:
                    return False
                tagname = code[i + 2: index]
                if not stack or stack[-1] != tagname:
                    return False
                stack.pop()
                i = index + 1 
            # 对于open tag来说 需要 1找到tag end 2.len要0-9 3.字符必须matchUppercase 4.压入栈
            elif code[i] == "<":
                index = code.find(">", i + 1)
                if index == -1:
                    return False
                
                tagname = code[i + 1: index]
                if len(tagname) > 9 or len(tagname) == 0:
                    return False 
                
                if not re.match(r"^[A-Z]+$", tagname):
                    return False
                stack.append(tagname)
                i = index + 1
            else:
                i += 1
        
        if not stack:
            return True
        return False
        

                    
print(Solution().isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))                   