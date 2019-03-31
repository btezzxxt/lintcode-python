class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        if originalString == "":
            return ""

        s = []
        for i in range(len(originalString)):
            if i == 0:
                count = 1
                char = originalString[i]
                continue
            
            if originalString[i] == originalString[i - 1]:
                count += 1
            else:
                s.append(char)
                s.append(str(count))
                count = 1
                char = originalString[i]
        s.append(char)
        s.append(str(count))

        if len(s) < len(originalString):
            return "".join(s) 
        return originalString

