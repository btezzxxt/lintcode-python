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


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 第二个办法有点浪费空间
from collections import deque
class Solution2:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        serial = []
        queue = deque([root])
        while queue:
            has_node = False
            
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not cur:
                    serial.append("#")
                    queue.append(None)
                    queue.append(None)
                else:
                    has_node = True
                    serial.append(str(cur.val))
                    queue.append(cur.left)
                    queue.append(cur.right)
            
            if not has_node:
                break
            
        temp = ",".join(serial)
        return temp
                    


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
        arr = data.split(",")
        root = self.construct(arr, 0)
        return root
        
    def construct(self, data, index):
        if index < len(data):
            if data[index] == "#":
                return None
            else:
                root = TreeNode(data[index])
                root.left = self.construct(data, index * 2 + 1)
                root.right = self.construct(data, index * 2 + 2)
                return root
        return None
        

from collections import deque
class Solution3:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return None
        
        data = []
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                data.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                data.append("#")
        string = ",".join(data)
        print(string)
        return string 
        

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
        if not data:
            return None 
        
        arr = data.split(",")
        root_val = arr[0]
        root = TreeNode(root_val)
        
        queue = deque([root])
        
        offset = 1
        while queue:
            n = len(queue)
            for i in range(len(queue)):
                cur = queue.popleft()
                left_val = arr[offset + i * 2]
                if left_val != '#':
                    cur.left = TreeNode(left_val)
                    queue.append(cur.left)
                right_val = arr[offset + i * 2 + 1]
                if right_val != "#":
                    cur.right = TreeNode(right_val)
                    queue.append(cur.right)
            offset += 2 * n
        return root
                
        
        
        