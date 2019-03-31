class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """
    # time out O(n2)
    # def pairNumbers(self, p):
    #     # Write your code here
    #     n = len(p)
    #     total = 0
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             if self.valid(p[i], p[j]):
    #                 total += 1 
    #     return total
    
    # def valid(self, p1, p2):
    #     if (p1.x + p2.x) % 2 == 0 and (p1.y + p2.y) % 2 == 0:
    #         return True
    #     return False 

    def pairNumbers(self, p):
        type_arr = [0, 0, 0, 0]
        
        # pair can only happen between the same type
        total = 0
        for point in p:
            res1, res2 = point.x % 2, point.y % 2
            if res1 == 0 and res2 == 0:
                type_arr[0] += 1
            elif res1 == 0:
                type_arr[1] += 1 
            elif res2 == 0:
                type_arr[2] += 1
            else: 
                type_arr[3] += 1
        
        for type_count in type_arr:
            if type_count == 0:
                total += 0
            else:
                # count 1 + 2 + 3 + 4 + ... + n = (1 + n) * n // 2
                x = type_count - 1 
                total += (1 + x) * x // 2
        return total

