# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        values = self.inorder(root, k)
        return values[k-1]

    def inorder(self, node, k):
        res = []
        if node:
            res = self.inorder(node.left, k)
            res.append(node.val)
            # k -= 1
            # if k == 0:
            #     return res[-1]
            res = res + self.inorder(node.right, k)
        return res

# Solution from leetcode (iterative)
class SolutionFast1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # find smallest
        walk = root
        stack = [walk]
        while walk.left != None:
            walk = walk.left
            stack.append(walk)
        walk = stack.pop()
        # step back repeatedly
        for i in range(1, k):
            if walk.right != None:
                walk = walk.right
                stack.append(walk)
                while walk.left != None:
                    walk = walk.left
                    stack.append(walk)
            walk = stack.pop()
        return walk.val

# Iterative
class SolutionF2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        l=[]
        while 1:
            while root:
                l.append(root)
                root=root.left
            node=l.pop()
            k-=1
            if not k:
                return node.val
            root=node.right