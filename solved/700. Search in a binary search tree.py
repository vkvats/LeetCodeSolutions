
# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# New Method
# Recursion
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return
        if root.val == val: return root
        elif root.val > val and root.left:
            return self.searchBST(root.left, val)
        elif root.val < val and root.right:
            return self.searchBST(root.right, val)

# iterative method
class SolutionIterative:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val: return node
            elif node.val< val and node.right:
                stack.append(node.right)
            elif node.val > val and node.left:
                stack.append(node.left)
            else: return




