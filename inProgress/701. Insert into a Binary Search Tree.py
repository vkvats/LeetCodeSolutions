# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        stack = [root]
        while stack:
            node = stack.pop()
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    stack.append(node.right)
            else:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    stack.append(node.left)
        return root

# method 2
class SolutionM2:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)

# Solution from leetcode

