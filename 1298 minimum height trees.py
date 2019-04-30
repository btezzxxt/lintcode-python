class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):
        # Wirte your code here
        if n == 1 and len(edges) == 0:
            return [0]
        
        
        indegree_map = {}
        neighbor_map = {}
        
        for i in range(n + 1):
            indegree_map[i] = 0 
            neighbor_map[i] = set()
            
        for edge in edges:
            indegree_map[edge[0]] += 1 
            indegree_map[edge[1]] += 1 
            neighbor_map[edge[0]].add(edge[1])
            neighbor_map[edge[1]].add(edge[0])
            
        leaves = set()
        for node, indegree in indegree_map.items():
            if indegree == 1:
                leaves.add(node)

        while leaves:
            n -= len(leaves)
            if n == 0:
                return list(leaves)
            
            next_leaves = set()
            for cur in leaves:
                for nb in neighbor_map[cur]:
                    if nb in indegree_map:
                        indegree_map[nb] -= 1 
                        neighbor_map[nb].remove(cur)
                        if indegree_map[nb] == 0 or indegree_map[nb] == 1:
                            next_leaves.add(nb)
            leaves = next_leaves
        return []       
        
print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))