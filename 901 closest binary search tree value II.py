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

    