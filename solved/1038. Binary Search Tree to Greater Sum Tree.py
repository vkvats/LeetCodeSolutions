## the solution is same as question 538
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convert(self, root: TreeNode, val: int):
        if root.right is not None:
            val = self.convert(root.right, val)

        val += root.val
        root.val = val

        if root.left is not None:
            val = self.convert(root.left, val)

        return val

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.convert(root, 0)
        return root

# iterative solution
class SolutionItr2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        total = 0
        stack = []
        current = root
        while True:
            if current != None:
                stack.append(current)
                current = current.right
            elif stack:
                current = stack.pop()
                total += current.val
                current.val = total
                current = current.left
            else:
                break
        return root