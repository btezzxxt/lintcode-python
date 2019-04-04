class GraphNode:
    def __init__(self, val):
        self.val = val
        self.nbs = []
        self.indegree = 0

from heapq import heappush, heappop, heapify
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        nodes, edges = self.create_graph(words)
        tp = self.get_topology(nodes, edges)
        seq = "".join(tp)
        return seq
        
    def get_zero_indegree(self, nodes):
        res = []
        for node in nodes.values():
            if node.indegree == 0:
                res.append(node.val)
        return res
        
    def sort(self, queue):
        if queue and queue[0] > queue[-1]:
            queue[0], queue[-1] = queue[-1], queue[0]
        
    
    def get_topology(self, nodes, edges):
        queue = self.get_zero_indegree(nodes)
        heapify(queue)

        tp = []
        while queue:
            cur = heappop(queue)
            tp.append(cur)
            cur_node = nodes[cur]
            for nb in cur_node.nbs:
                nodes[nb].indegree -= 1 
                if nodes[nb].indegree == 0:
                    heappush(queue, nb)

        if len(tp) == len(nodes):
            return tp 
        else:
            return []
            
        
    def create_graph(self, words):
        nodes = {}
        edges = set()
        
        for word in words:
            for char in word:
                if char not in nodes:
                    nodes[char] = GraphNode(char)
        
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                char1 = words[i][j]
                char2 = words[i + 1][j]
                if char1 != char2:
                    edges.add((char1, char2))
                    break
        
        for edge in edges:
            # for a -> b
            a = edge[0]
            b = edge[1]
            
            nodes[a].nbs.append(b)
            nodes[b].indegree += 1         
        return nodes, edges
   