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

class Solution2:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s: int, k: int) -> int:
        # write your code here
        if k == 0:
            return 0

        used = {}
        i = 0
        j = 0
        count = 0
        maxcount = 0
        while i < len(s):
            if s[i] not in used:
                if len(used) >= k:
                    # remove one item from used
                    while j < i:
                        if used[s[j]] == 1:
                            del used[s[j]]
                            count -= 1
                            j += 1
                            break
                        else:
                            used[s[j]] -= 1
                            count -= 1
                            j += 1
            used[s[i]] = 1
            count += 1
            i += 1
            maxcount = max(count, maxcount)
        return maxcount


