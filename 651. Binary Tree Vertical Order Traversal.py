"""
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Example
Example1

Inpurt:  {3,9,20,#,#,15,7}
Output: [[9],[3,15],[20],[7]]
Explanation:
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Example2

Input: {3,9,8,4,0,1,7}
Output: [[4],[9],[3,0,1],[8],[7]]
Explanation:
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

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
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        val_map = self.helper(root)

        items = []
        for (index, arr) in val_map.items():
            items.append((index, arr))
        
        items.sort(key=lambda x: x[0])
        res = []
        for item in items:
            res.append(item[1])
        return res 



    def helper(self, root):
        if not root:
            return {}

        val_map = {} 
        
        queue = deque([(root, 0)])
        while queue:
            cur, index = queue.popleft()
            if index in val_map:
                val_map[index].append(cur.val)
            else:
                val_map[index] = [cur.val]

            if cur.left:
                queue.append((cur.left, index - 1))
            if cur.right:
                queue.append((cur.right, index + 1))
        return val_map 