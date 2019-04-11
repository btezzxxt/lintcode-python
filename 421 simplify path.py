class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        # write your code here
        if len(path) == 0:
            return path
        
        stack = []
        directory = []

        n = len(path)
        i = 0
        while i < n:
            char = path[i]
            if char == "/" and path[i: i + 3] == "/.." and (i + 3 == n or path[i + 3] == "/"):
                if stack:
                    stack.pop()
                i = i + 3
            elif char == "/" and path[i: i + 2] == "/." and (i + 2 == n or path[i + 2] == "/"):
                i = i + 2             
            elif char == "/":
                i = i + 1
            elif char != "/" and (i + 1 == n or path[i + 1] == "/"):
                directory.append(char)
                stack.append("".join(directory))
                directory = []
                i = i + 1
            else:
                directory.append(char)
                i = i + 1
        final = "/"
        if not stack:
            return final

        final += "/".join(stack)
        return final                
print(Solution().simplifyPath("/.hidden"))


            

                 

