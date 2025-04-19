# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# get all values on nodes using inorder traversal and then check if the condition is satisfied.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        nodes = self.inorder(root)
        for i in range(len(nodes) - 1):
            if nodes[i] >= nodes[i + 1]:
                return False
        return True

    def inorder(self, node):
        arr = []
        if node:
            arr = self.inorder(node.left)
            arr.append(node.val)
            arr = arr + self.inorder(node.right)
        return arr

# in order traversal (iterative version)
class SolutionItr:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True