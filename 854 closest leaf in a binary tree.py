"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


from collections import deque
class Solution:
    """
    @param root: the root
    @param k: an integer
    @return: the value of the nearest leaf node to target k in the tree
    """
    def findClosestLeaf(self, root, k):
        # Write your code here
        # every node val is unique means we could use map save (node, parent) thus tree becomes a graph
        parent = {}
        parent[root] = root
        target = self.dfs(root, k, parent)

        queue = deque([target])
        
        visited = set()
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                visited.add(cur)
                if not cur.left and not cur.right:
                    return cur.val 
                
                if cur.left and cur.left not in visited:
                    queue.append(cur.left)
                
                if cur.right and cur.right not in visited:
                    queue.append(cur.right)
                
                if parent[cur] not in visited:
                    queue.append(parent[cur])
        raise "Error" 
        
    def dfs(self, root, k, parent):
        temp = None
        if root.val == k:
            temp = root
        
        if not root.left and not root.right:
            return temp 
        
        if root.left:
            parent[root.left] = root 
            left_k = self.dfs(root.left, k, parent)
            if left_k:
                temp = left_k
        
        if root.right:
            parent[root.right] = root 
            right_k = self.dfs(root.right, k, parent)
            if right_k:
                temp = right_k 
        return temp
        
        