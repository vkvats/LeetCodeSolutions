# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        if not root:
            return ""
        root.val = str(root.val)
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                output.append(node.val)
            if node.left:
                node.left.val = node.val + "->" + str(node.left.val)
                stack.append(node.left)
            if node.right:
                node.right.val = node.val + "->" + str(node.right.val)
                stack.append(node.right)
        return output

# solution from leetcode
class SolutionFast1:
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        paths = []
        path = ''
        self.preorder(root, path, paths)
        return paths

    def preorder(self, root, path, paths):
        if not root:
            return
        path += str(root.val) + '->'
        self.preorder(root.left, path, paths)
        self.preorder(root.right, path, paths)
        if not root.left and not root.right:
            path = path[:-2]
            paths.append(path)