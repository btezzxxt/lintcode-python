class Solution:
    """
    @param mat: The matrix
    @return: The answer
    """
    def findingNumber(self, mat):
        # Write your code here
        if not mat and not mat[0]:
            return -1
        
        count_map = {}
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            layer_count = set()
            for j in range(n):
                val = mat[i][j]
                layer_count.add(val)
              
            for uniq in layer_count:
                if uniq in count_map:
                    count_map[uniq] += 1 
                else:
                    count_map[uniq] = 1 
        
        min_val = 1000001
        for val, count in count_map.items():
            if count == m:
                min_val = min(min_val, val)
        
        if min_val == 1000001:
            return -1 
        return min_val