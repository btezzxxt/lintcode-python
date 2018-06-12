class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        map = {}
        max_c = 0
        j = 0
        for i, v_back in enumerate(s):
            while j < len(s):
                c = s[j]
                if c in map:
                    map[c] += 1
                else:
                    if len(map) < k:
                        map[c] = 1
                    else:
                        break

                max_c = max(max_c, j - i + 1)
                j += 1
            
            c2 = s[i]
            if c2 in map:
                if map[c2] > 1:
                    map[c2] -= 1
                else:
                    del map[c2]
        return max_c