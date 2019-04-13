class Solution:
    """
    @param source: List[str]
    @return: return List[str]
    """
    def removeComments(self, source):
        # write your code here
        res = []
        buffer = []
        comment_open = False

        for line in source:
            i = 0
            length = len(line)
            while i < length:
                char = line[i]
                if char == "/" and i + 1 < length and line[i + 1] == "/" and not comment_open:
                    i = length      
                elif char == "/" and i + 1 < length and line[i + 1] == "*" and not comment_open:
                    comment_open = True 
                    i = i + 2
                elif char == "*" and i + 1 < length and line[i + 1] == "/" and comment_open:
                    comment_open = False
                    i = i + 2
                elif not comment_open:
                    buffer.append(char)
                    i = i + 1
                else:
                    i = i + 1 
            if not comment_open and buffer:
                res.append("".join(buffer))
                buffer = []
        return res

source =["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print(Solution().removeComments(source))

