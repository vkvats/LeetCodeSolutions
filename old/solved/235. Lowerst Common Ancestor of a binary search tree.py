# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        while stack:
            node = stack.pop()
            if (node.val > p.val and node.val < q.val) or (node.val < p.val and node.val > q.val):
                if node.left and node.right:
                    return node
            # if node.val == p.val:
            #     if node.left:
            #         if node.left.val == q.val:
            #             return node
            #     if node.right:
            #         if node.right.val == q.val:
            #             return node
            if node.val == p.val and node.val > q.val: return node
            if node.val == p.val and node.val < q.val: return node
            if node.val == q.val and node.val < p.val: return node
            if node.val == q.val and node.val > p.val: return node

            # if node.val == q.val:
            #     if node.left:
            #         if node.left.val == p.val:
            #             return node
            #     if node.right:
            #         if node.right.val == p.val:
            #             return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

# Solution from leetcode (fast)
class SolutionFast1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

# 