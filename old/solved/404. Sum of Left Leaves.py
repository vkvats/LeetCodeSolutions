# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        left_leaves = []
        while stack:
            node = stack.pop()
            # add left node
            if node.left:
                stack.append(node.left)
                # visit
                if not node.left.left and not node.left.right:
                    left_leaves.append(node.left.val)
            # add right node.
            if node.right:
                stack.append(node.right)
        return sum(left_leaves)

# Solution from leetcode
class SolutionFast1:
    def __init__(self):
        self.total = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.total

    def dfs(self, root):
        # base case
        if not root: return
        # visit
        if root.left:
            if not root.left.left and not root.left.right:
                self.total += root.left.val
        # recurssive call.
        self.dfs(root.left)
        self.dfs(root.right)

# solution from leetCode
class SolutionFast2:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def traverse(node, left):
            ret_val = 0
            if not node.left and not node.right and left:
                ret_val = node.val
            else:
                if node.left:
                    ret_val += traverse(node.left, True)
                if node.right:
                    ret_val += traverse(node.right, False)
            return ret_val
        if root is None:
            return 0
        return traverse(root, False)

# Solution from leetCode
# Definition for a binary tree node.
def isLeaf(root: TreeNode):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False


class Solution:

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        if root is not None:

            # if the nodes left is another node, traverse
            # else add to total

            if isLeaf(root.left):
                total += root.left.val

            else:
                total += self.sumOfLeftLeaves(root.left)

            total += self.sumOfLeftLeaves(root.right)

        return total


# solution from leetcode
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def walk(root, isleft):

            if not root:
                return 0
            if not root.left and not root.right and isleft:
                return root.val
            return walk(root.left, True) + walk(root.right, False)

        return walk(root, False)