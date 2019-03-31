"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# iteration
from collections import deque
class Solution2:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        # Write your code here
        if root == None:
            return True
        
        queue = deque([root])

        while queue:
            numbers = []
            has_next_round = False
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    numbers.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)   
                    has_next_round = True
                else:
                    numbers.append("#")
                    queue.append(None)
                    queue.append(None)                       

            if not self.is_numbers_symmetric(numbers):
                return False
                
            if not has_next_round:
                break
        return True
    
    def is_numbers_symmetric(self, numbers):
        if len(numbers) <= 1:
            return True
        
        l = 0 
        r = len(numbers) - 1 

        while l < r:
            if numbers[l] != numbers[r]:
                return False
            l += 1 
            r -= 1 
        return True

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself 
    """
    def isSymmetric(self, root):
        if root == None:
            return True
        
        return self.is_chilren_sym(root.left, root.right)

    
    def is_two_tree_sym(self, left, right):
        if not left and not right:
            return True
        elif if not left or not right:
            return False

        if left.val != right.val:
            return False
        
        return self.is_two_tree_sym(left.left, right.right) and self.is_two_tree_sym(left.right, right.left)