class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


from collections import deque
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ""
        arr = []
        queue = deque([root])
        
        while queue:
            cur = queue.popleft()
            if cur:
                arr.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                arr.append('#')
        str_ = ','.join(arr)
        return str_

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == "":
            return None

        data = data.split(',')
        rootVal = data[0]
        root = TreeNode(rootVal)
        queue = deque([root])
        level_end_index = 0
        while queue:
            curLen = len(queue)
            for level_index in range(len(queue)):
                curNode = queue.popleft()
                leftData = data[level_end_index + level_index * 2 + 1]
                if leftData != '#':
                    left = TreeNode(leftData)
                    curNode.left = left
                    queue.append(left)
                rightData = data[level_end_index + level_index * 2 + 2]
                if rightData != '#':
                    right = TreeNode(rightData)
                    curNode.right = right
                    queue.append(right)
            level_end_index += curLen * 2
        return root
Solution().deserialize("123####")
