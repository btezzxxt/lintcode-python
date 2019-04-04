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
        