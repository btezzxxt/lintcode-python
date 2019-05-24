class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        counter = {}
        for task in tasks:
            if task in counter:
                counter[task] += 1 
            else:
                counter[task] = 1 
        
        max_count = max(counter.values())
        total_count = len(tasks)
        
        spaces_in_between = (max_count - 1) * n 
        longest = max_count + spaces_in_between
        
        for count in counter.values():
            if count == max_count:
                longest += 1 
        longest -= 1 
        
        return max(longest, total_count)
        
import collections
class Solution2:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        counter = collections.defaultdict(int)
        for task in tasks:
            counter[task] += 1 
        
        n = len(tasks)
        max_count = max(counter.values())
        total = (max_count - 1) * (n + 1) + 1 
        
        max_count_tasks = -1 
        for count in counter.values():
            if count == max_count:
                max_count_tasks += 1 
        
        if max_count_tasks <= n:
            total += max_count_tasks
        
        return max(total, n)

print(Solution2().leastInterval("AAABBB", 2))