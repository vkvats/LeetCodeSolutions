# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        level = 0
        while stack:
            stack, level = self.pop(stack, level)
        return level

    def pop(self, array, level):
        level += 1
        children = []
        while array:
            node = array.pop()
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

# from leetcode (recursive)
class SolutionFast1:
    def maxDepth(self, root: TreeNode) -> int:

        # edge cases
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Recursive
class SolutionFast2:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0;
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right));

# top-down and bottom up approach
class Solution:
    ## top-down
    def getDepth(self, node, depth):
        if node:
            return max(self.getDepth(node.left, depth + 1), self.getDepth(node.right, depth + 1))
        else:
            return depth

    ## bottom-up
    def getSubDepth(self, node):
        if not node:
            return 0
        else:
            return max(self.getSubDepth(node.left), self.getSubDepth(node.right)) + 1

    def maxDepth(self, root: TreeNode) -> int:

        return self.getDepth(root, 0)
        # return self.getSubDepth(root)