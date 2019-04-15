"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        if not root:
            return []
        
        left = self.get_left(root, [])
        right = self.get_right(root, [])
        bot = self.get_bot(root, [])
        
        if not root.left and not root.right:
            return [root.val]
        elif not root.left:
            if root.val != bot[0]:
                bot = [root.val] + bot 
            if bot[-1] == right[0]:
                bot.pop()
            return bot + right
        elif not root.right:
            if left[-1] == bot[0]:
                left.pop()
            return left + bot 
        else:
            if left[-1] == bot[0]:
                left.pop() 
            
            if bot[-1] == right[0]:
                bot.pop()
            return left + bot + right
        
        return left + bot + right
        
    def get_bot(self, root, arr):
        stack = []
        while root:
            stack.append(root)
            root = root.left 
        
        while stack:    
            cur = stack.pop()
            if not cur.left and not cur.right:
                arr.append(cur.val)
            
            if cur.right:
                node = cur.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = cur
                while stack and stack[-1].right == node:
                    node = stack.pop()
        return arr 
        
    def get_left(self, root, arr):
        while root:
            arr.append(root.val)
            if root.left:
                root = root.left
            else:
                root= root.right
        return arr 
    
    def get_right(self, root, arr):
        while root:
            arr.append(root.val)
            if root.right:
                root = root.right 
            else:
                root = root.left
        arr.reverse()
        # pop root
        arr.pop()
        return arr 
            
            
            
            
        
    