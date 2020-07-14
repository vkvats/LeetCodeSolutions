# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: #iterative
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root and sum == 0:
            return False
        elif not root:
            return False
        root.val = sum - root.val
        stack = [root]

        while stack:
            node = stack.pop()
            if self.is_leaf(node) and node.val == 0: return True

            if node.right:
                node.right.val = node.val - node.right.val
                stack.append(node.right)
            if node.left:
                node.left.val = node.val - node.left.val
                stack.append(node.left)
        return False

    def is_leaf(self, node):
        if not node.left and not node.right:
            return True
        else:
            return False
# Iterative
class SolutionItr2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [root]
        while stack:
            current = stack.pop()
            if current.val == sum and not current.left and not current.right:
                return True

            if current.left:
                current.left.val += current.val
                stack.append(current.left)

            if current.right:
                current.right.val += current.val
                stack.append(current.right)

        return False

# Recursive
class SolutionRec:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)