# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        value = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != value:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True


# fastest solution from leetcode (Recursive)
class Solution:
    def isUnivalTree(self, root) -> bool:
        if not root:
            return False
        target = root.val

        def dfs(root, target):
            if not root:
                return True
            if root.val != target:
                return False
            return dfs(root.left, target) and dfs(root.right, target)

        return dfs(root, target)