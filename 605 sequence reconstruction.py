from collections import defaultdict, deque
class Solution:

    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        nodes = set()
        for seq in seqs:
            nodes |= set(seq)
        
        edges = set()
        for seq in seqs:
            for i in range(len(seq)):
                if i > 0 and (seq[i - 1], seq[i]) not in edges:
                    edges.add((seq[i - 1], seq[i]))

        indegree = defaultdict(int)
        for node in nodes:
            indegree[node] = 0
        
        neighbors = defaultdict(list)
        for edge in edges:
            indegree[edge[1]] += 1
            neighbors[edge[0]].append(edge[1])
        
        # get indegree == 0s
        queue = deque([])
        for key in indegree.keys():
            if indegree[key] == 0:
                queue.append(key)
        
        res = []
        while len(queue) == 1: # only one item in queue at the same time makes the unique sorting; otherwise multiple topology
            cur = queue.popleft()
            res.append(cur)
            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(queue) > 1:
            return False
        
        return org == res

print(Solution().sequenceReconstruction([1,2,3], [[1,2],[1,3],[2,3]]))