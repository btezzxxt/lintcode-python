class Solution2:
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


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        return self.dfs(pattern, str, {}, set())
        
    # 用pattern map来确认pattern对应的字符串
    # 用used来确保一个str子串只能对应一个pattern
    def dfs(self, pattern, str, pattern_map, used):
        if str == "" and pattern == "":
            return True
        elif str == "":
            return False
        elif pattern == "":
            return False
        
        p = pattern[0]
        if p not in pattern_map:
            for i in range(len(str)):
                match_str = str[: i + 1]
                if match_str in used:
                    continue
                pattern_map[p] = match_str
                used.add(match_str)
                if self.dfs(pattern[1:], str[i + 1:], pattern_map, used):
                    return True
                del pattern_map[p]
                used.remove(match_str)
            return False
        else:
            match_str = pattern_map[p]
            if str.startswith(match_str):
                return self.dfs(pattern[1:], str[len(match_str):], pattern_map, used)
            else:
                return False
            
        
        
print(Solution().wordPatternMatch("aaaa", "dogdogdogdog"))