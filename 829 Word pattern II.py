class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.dfs(pattern, str, set(), {})
    
    def dfs(self, pattern, str, used_str, pattern_map):
        if len(pattern) == 0 and len(str) == 0:
            return True

        if len(str) == 0 or len(pattern) == 0:
            return False
        
        cur_p = pattern[0]
        if cur_p in pattern_map:
            match = pattern_map[cur_p]
            return match == str[:len(match)] and self.dfs(pattern[1:], str[len(match):], used_str, pattern_map)
        else:
            for i in range(1, len(str) + 1):
                try_match = str[:i]
                if try_match not in used_str:
                    used_str.add(try_match)
                    pattern_map[cur_p] = try_match
                    is_match = self.dfs(pattern[1:], str[i:], used_str, pattern_map)
                    if is_match:
                        return True
                    used_str.remove(try_match)
                    del pattern_map[cur_p]
        return False

print(Solution().wordPatternMatch("d", "ed"))