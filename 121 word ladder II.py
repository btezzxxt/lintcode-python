from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    # bfs 从end到start，确定最短需要的步数和路径上，dict中每一个单词到end的距离。然后从start开始按步数-1进行dfs寻找所有最短解
    def findLadders(self, start, end, dict):
        # write your code here
        step_map = {}
        res = []
        dict.add(end)
        dict.add(start)
        min_step = self.bfs_steps_to_end(start, end, dict, step_map)
        self.dfs_get_paths(start, end, dict, step_map, min_step, [start], res)
        return res

    # start from end, looking for the start
    def bfs_steps_to_end(self, start, end, dict, step_map):
        queue = deque([end])
        step_map[end] = 0
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                words = self.get_next_words(cur, dict)
                for word in words:
                    if word not in step_map:
                        if word == start:
                            return step
                        step_map[word] = step
                        queue.append(word)
         

    def dfs_get_paths(self, start, end, dict, step_map, cur_step, path, res):
        if cur_step == 0 and start == end:
            res.append(list(path))
            return 

        if cur_step <= 0:
            return
        
        words = self.get_next_words(start, dict)
        for word in words:
            if word in step_map and step_map[word] == cur_step - 1:
                path.append(word)
                self.dfs_get_paths(word, end, dict, step_map, cur_step - 1, path, res)
                path.pop()
    
    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for l in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] != l:
                    newword = word[:i] + l + word[i + 1:]
                    if newword in dict:
                        words.append(newword)
        return words
