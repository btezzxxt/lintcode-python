class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        lbs = self.getStack(root, target)
        ubs = lbs[:]

        if lbs[-1].val > target:
            self.getLowerNext(lbs)
        else:
            self.getUpperNext(ubs)


        res = []
        while k > 0:
            
            if ubs and lbs:
                if abs(ubs[-1].val - target) < abs(lbs[-1].val - target):
                    res.append(ubs[-1].val)
                    self.getUpperNext(ubs)
                else:
                    res.append(lbs[-1].val)
                    self.getLowerNext(lbs)
            elif lbs:
                res.append(lbs[-1].val)
                self.getLowerNext(lbs)
            elif ubs:
                res.append(ubs[-1].val)
                self.getUpperNext(ubs)
            else:
                return []

            # 用while循环一定要写这个k -= 1 要不然就用forloop
            k -= 1
        return res

    # get a path to either the closest lowerbound or upperbound of target in a stack
    def getStack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return stack
        return stack

    def getUpperNext(self, stack):
        nxt = stack[-1]
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
        return nxt

    def getLowerNext(self, stack):
        nxt = stack[-1]
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
        return nxt

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

class Solution2:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        if root == None:
            return []
        
        path = []
        cur = root
        while cur:
            path.append(cur)
            if cur.val == target:
                break
            elif cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
                
        path_pre = path[::]
        last_node = path[-1]
        self.get_next(path)
        self.get_pre(path_pre)
        
        smaller, bigger = None, None
        if last_node.val <= target:
            smaller = last_node
            bigger = self.get_next(path)
            
        else:
            smaller = self.get_pre(path_pre)
            bigger = last_node
        
        res = []
        for i in range(k):    
            if smaller and bigger:
                print(smaller.val, bigger.val)
                if abs(smaller.val - target) <= abs(bigger.val - target):
                    res.append(smaller.val)
                    smaller = self.get_pre(path_pre)
                else:
                    res.append(bigger.val)
                    bigger = self.get_next(path)

            
            elif smaller:
                res.append(smaller.val)
                print(res, path_pre)
                smaller = self.get_pre(path_pre)
            else:
                res.append(bigger.val)
                bigger = self.get_next(path)
        return res
    
    def get_next(self, stack):
        if len(stack) == 0:
            return None
        
        node = stack[-1]
        if node.right:
            cur = node.right
            while cur:
                stack.append(cur)
                cur = cur.left
        else:
            cur = stack.pop()
            while stack and stack[-1].right == cur:
                cur = stack.pop()
        return node
        
    def get_pre(self, stack):
        if len(stack) == 0:
            return None
        
        node = stack[-1]
        if node.left:
            cur = node.left
            while cur:
                stack.append(cur)
                cur = cur.right
        else:
            cur = stack.pop()
            while stack and stack[-1].left == cur:
                cur = stack.pop()
        return node
    

        
            
        
            
        
    def get_next(self, stack):
        if len(stack) == 0:
            return None
        
        node = stack[-1]
        if node.right:
            cur = node.right
            while cur:
                stack.append(cur)
                cur = cur.left
        else:
            cur = stack.pop()
            while stack and stack[-1].right == cur:
                cur = stack.pop()
        return node
        
    def get_pre(self, stack):
        if len(stack) == 0:
            return None
        
        node = stack[-1]
        if node.left:
            cur = node.left
            while cur:
                stack.append(cur)
                cur = cur.right
        else:
            cur = stack.pop()
            while stack and stack[-1].left == cur:
                cur = stack.pop()
        return node
    
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
d.left = b
d.right = e
b.left = a
b.right = c

print(Solution2().closestKValues(d, 3.7, 3))
