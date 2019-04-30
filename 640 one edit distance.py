class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here

        if abs(len(s) - len(t)) > 1:
            return False 

        if len(s) == len(t):
            diff_found = False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if not diff_found:
                        diff_found = True
                    else:
                        return False 
            return True if diff_found else False 
        else:
            if len(s) > len(t):
                t, s = s, t 
            diff_found = False 
            i = 0
            j = 0
            while i < len(s):
                if s[i] != t[j]:
                    if not diff_found:
                        diff_found = True 
                        j += 1 
                    else:
                        return False            
                i += 1 
                j += 1
            
            if i == j or diff_found:
                return True 
            return False

print(Solution().isOneEditDistance("a", "ab"))