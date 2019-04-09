class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """
    def compareVersion(self, version1, version2):
        # Write your code here
        versions1 = self.process(version1)
        versions2 = self.process(version2)
        
        max_len = max(len(versions1), len(versions2))
        for i in range(max_len):
            v1 = versions1[i] if i < len(versions1) else 0 
            v2 = versions2[i] if i < len(versions2) else 0 
            if v1 < v2:
                return -1 
            elif v1 > v2:
                return 1 
            else:
                continue
        return 0
            
        
    def process(self, version):
        parts = version.split(".")
        versions = []
        for part in parts:
            versions.append(self.stoi(part))
        return versions
    
    def stoi(self, s):
        s = s.strip()
        if s == "":
            return 0 
        
        num = 0
        for char in s:
            num = num * 10 + int(char)
        return num 
        