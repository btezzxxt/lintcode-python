from collections import deque
class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns 
    """
    # 巨多的坑，要注意1 int 变str 2 数组reference要copy 3 0 往下拨是9
    def openLock(self, deadends, target):
        # Write your code here
        lock = [0, 0, 0, 0]

        visited = set()
        for deadend in deadends:
            if deadend == "0000":
                return -1
            
            visited.add(deadend)
            
        queue = deque([lock])
        
        step = -1
        while queue:
            step += 1 
            for _ in range(len(queue)):
                cur = queue.popleft()
                if self.itos(cur) == target:
                    return step
                    
                for i in range(4):
                    cur1 = cur[::]
                    cur1[i] = (cur1[i] + 1) % 10
                    cur2 = cur[::]
                    
                    if cur2[i] == 0:
                        cur2[i] = 9
                    else:
                        cur2[i] -= 1
                    
                    if cur1[i] >= 0 and cur1[i] <= 9 and self.itos(cur1) not in visited:
                        queue.append(cur1)
                        visited.add(self.itos(cur1))
                    
                    if cur2[i] >= 0 and cur2[i] <= 9 and self.itos(cur2) not in visited:
                        queue.append(cur2)
                        visited.add(self.itos(cur2))
                    
        return -1
        
    def itos(self, int_arr):
        string = ""
        for num in int_arr:
            string += str(num)
        return string