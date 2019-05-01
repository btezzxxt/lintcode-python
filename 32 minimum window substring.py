class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not source or not target:
            return ""
        
        target_map = {}
        for char in target:
            self.add_to_map(target_map, char)
        
        has_map = {}      
        l = 0
        r = 0
        
        res = None 
        while r < len(source):
            while r < len(source) and not self.containall(has_map, target_map):
                char = source[r]    
                self.add_to_map(has_map, char)
                r += 1 
            
            while l < r:
                char = source[l]
                l += 1 
                self.remove_from_map(has_map, char)
                if not self.containall(has_map, target_map):
                    break
            
            self.add_to_map(has_map, source[l - 1])
            if self.containall(has_map, target_map):
                temp = source[l - 1: r]
                if res == None:
                    res = temp
                else:
                    if len(res) > len(temp):
                        res = temp
                self.remove_from_map(has_map, source[l - 1])


        return res if res != None else ""  
        
    def add_to_map(self, map, char):
        if char in map:
            map[char] += 1 
        else:
            map[char] = 1 
    
    def remove_from_map(self, map, char):
        if char in map:
            map[char] -= 1 
            if map[char] == 0:
                del map[char]
                
    def containall(self, map_s, map_target):
        for char, count in map_target.items():
            if char not in map_s or map_s[char] < count:
                return False 
        return True
        
        