# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def leaf(self, node):
        if not node.left and not node.right:
            return True
        return False

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        stack1, stack2 = [root1], [root2]
        leaf1, leaf2 = [], []
        leaf1 = self.traverse(stack1, leaf1)
        leaf2 = self.traverse(stack2, leaf2)
        if tuple(leaf1) == tuple(leaf2):
            return True
        return False

    def traverse(self, stack, leaf):
        while stack:
            node = stack.pop()
            if self.leaf(node):
                leaf.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaf

# Solution From leetcode (Recursive)
class SolutionFast1:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        leaves1 = []
        leaves2 = []

        self.recv(root1, leaves1)
        self.recv(root2, leaves2)

        if len(leaves1) != len(leaves2):
            return False

        i = 0
        while i < len(leaves1):

            if leaves1[i] != leaves2[i]:
                return False

            i += 1

        return True

    def recv(self, root, leaves):

        if root == None:
            return

        # Leaf
        if (root.left == None) and (root.right == None):
            leaves.append(root.val)

        else:

            self.recv(root.left, leaves)
            self.recv(root.right, leaves)

# recursive concise
class SolutionRecuur:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            res = []
            def _dfs(node):
                if not node: return
                if not node.left and not node.right:
                    res.append(node.val)
                _dfs(node.left)
                _dfs(node.right)
            _dfs(root)
            return res
        return dfs(root1) == dfs(root2)
