# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                stack.append(node.left)
                stack.append(node.right)
                node.left, node.right = node.right, node.left
            elif node.left and not node.right:
                stack.append(node.left)
                node.right = node.left
                node.left = None
            elif not node.left and node.right:
                stack.append(node.right)
                node.left = node.right
                node.right = None
        return root
# Solution from leetcode (Recursive)
class SolutionFast1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invertHelper(root)

        return root

    def invertHelper(self, node):
        if node is None:
            return

        node.right, node.left = node.left, node.right
        self.invertHelper(node.left)
        self.invertHelper(node.right)

# solution from leetcode (recursive)
class SolutionFast2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# 
