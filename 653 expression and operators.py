class Solution:
    """
    @param num: a string contains only digits 0-9
    @param target: An integer
    @return: return all possibilities
    """
    def addOperators(self, num, target):
        # write your code here
        res = []
        
        self.dfs(num, 0, 0, 0, target, "", res)
        return res
    
    def dfs(self, num, start, total, lastnum, target, path, res):
        if start == len(num) and total == target:
            res.append(path)
            return 
        
        for i in range(start + 1, len(num) + 1):
            number_str = num[start: i]
            number = int(number_str)
            
            if start == 0:
                self.dfs(num, i, total + number, number, target, number_str, res)
            else:
                self.dfs(num, i, total + number, number, target, path + "+" + number_str, res)

                self.dfs(num, i, total - number, -number, target, path + "-" + number_str, res)

                self.dfs(num, i, total - lastnum + lastnum * number, lastnum * number, target, path + "*" + number_str, res)
                
            # anything that starts with 0. only 0 is valid
            if number == 0:
                break
class Solution2:
    def addOperators(self, num, target):
        def dfs(idx, tmp, tot, last, res):
            if idx == len(num):
                if tot == target:
                    res.append(tmp)
                return
            for i in range(idx, len(num)):
                x = int(num[idx: i + 1])
                if idx == 0:
                    dfs(i + 1, str(x), x, x, res)
                else:
                    dfs(i + 1, tmp + "+" + str(x), tot + x, x, res)
                    dfs(i + 1, tmp + "-" + str(x), tot - x, -x, res)
                    dfs(i + 1, tmp + "*" + str(x), tot - last + last * x, last * x, res)
                if x == 0:
                    break
        res = []
        dfs(0, "", 0, 0, res)
        return res
print(Solution().addOperators("0030", 3))