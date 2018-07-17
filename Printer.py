from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Printer:
    @staticmethod
    def tree(root):
        res = []
        que = deque()
        que.append(root)
        while que:
            cur = que.popleft()
            if cur:
                res.append(cur.val)
                que.append(cur.left)
                que.append(cur.right)
            else:
                res.append('#')
        print(res)
