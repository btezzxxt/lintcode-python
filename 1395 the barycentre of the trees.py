import collections, sys
class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    
    node = sys.maxsize
    max_sub = sys.maxsize
    
    def getBarycentre(self, x, y):
        # Write your code here
        graph = collections.defaultdict(set)
       
        for i in range(len(x)):
            graph[x[i]].add(y[i])
            graph[y[i]].add(x[i])

        n = len(graph.keys())
        maxtree_of_node = [0] * (n + 1)

        self.dfs(1, 0, maxtree_of_node, n, graph)
        return self.node 
    
    def dfs(self, cur_node, prev_node, maxtree_of_node, n, graph):
        
        maxtree_of_node[cur_node] = 1 
        max_sub_local = 0
        for node in graph[cur_node]:
            if node == prev_node:
                continue 
            
            self.dfs(node, cur_node, maxtree_of_node, n, graph)
            maxtree_of_node[cur_node] += maxtree_of_node[node]
            max_sub_local =  max(max_sub_local, maxtree_of_node[node])
        max_sub_local = max(max_sub_local, n - maxtree_of_node[cur_node])
        
        if max_sub_local < self.max_sub or (max_sub_local == self.max_sub and cur_node < self.node):
            self.node = cur_node 
            self.max_sub = max_sub_local

print(Solution().getBarycentre([1,2,2], [2,3,4]))