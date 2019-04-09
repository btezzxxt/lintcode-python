import sys
class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

class Solution:
    """
    @param x: The end points of edges set
    @param y: The end points of edges set
    @param d: The weight of points set
    @return: Return the maximum product
    """
    def getProduct(self, x, y, d):
        # Write your code here
        # construct tree 
        node_map = {}
        for i in range(len(d)):
            node = Node(d[i])
            node_map[i + 1] = node 
            
        for i in range(len(x)):
            parent = node_map[x[i]]
            child = node_map[y[i]]
            if not parent.left:
                parent.left = child
            else:
                parent.right = child 
        
        root = node_map[1]
        
        products = []
        self.dfs(root, [root.val], products)
        
        return max(products) 
        
    def dfs(self, root, path, products):
        if not root.left and not root.right:
            res = 1
            for num in path:
                res *= (num % (1e9 + 7))
            products.append(res % (1e9 + 7))
        
        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, path, products)
            path.pop()
        
        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, path, products)
            path.pop()
            
print(Solution().getProduct([1,2,2], [2,3,4], [1,1,-1,2]))  
            
        
        
        
        
        
        
        
        