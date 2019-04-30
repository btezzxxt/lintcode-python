class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        # Write your code here
        if not color:
            return ""
        
        res = "#"
        for i in range(1, 7, 2):
            res += self.get_near_hex(color[i], color[i + 1])
        return res 
        
    def get_near_hex(self, char1, char2):
        val = int(char1, 16) * 16 + int(char2, 16)
        remain = val % 17 
        mutiply = val // 17
        if remain > val / 2:
            mutiply += 1 
        
        close_hex = mutiply * 17 
        hex_num = mutiply // 16
        if hex_num >= 10:
            hex_char = chr(hex_num - 10 + ord('a'))
        else:
            hex_char = str(hex_num)
        return hex_char + hex_char
        
        
        
            
        