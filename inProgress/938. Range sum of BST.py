## Solution from leetcode using queue
class Solution:
    def rangeSumBST(self, root , L: int, R: int) -> int:
        sum = 0
        if root is None:
            return sum
        queue = []
        queue.append(root)
        while (queue):
            current = queue.pop()
            if L<= current.val and R >= current.val:
                sum += current.val
            if current.left is not None and current.val > L:
                queue.append(current.left)
            if current.right is not None and current.val < R:
                queue.append(current.right)
        return sum



# solution DFS
class SolutionDFS:
    def rangeSumBST(self, root, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L<=node.val<=R:
                    self.ans+=node.val
                if L<node.val:
                    dfs(node.left)
                if node.val<R:
                    dfs(node.right)
        self.ans=0
        dfs(root)
        return self.ans



## solution from leetcode
class SolutionFast:
    def rangeSumBST(self, root: , L: int, R: int) -> int:
        while root:
            if root.val < L:
                root = root.right
            elif root.val > R:
                root = root.left
            else:
                self.sum = 0
                self.range_sum(root, L, R)
                break
        return self.sum

    def range_sum(self, node, L, R):
        if node:
            if L <= node.val <= R:
                self.sum += node.val
            if node.val > L:  # remove this condition if it's confusing but it should theoretically speed things up
                self.range_sum(node.left, L, R)
            if node.val < R:  # remove this condition if it's confusing but it should theoretically speed things up
                self.range_sum(node.right, L, R)

# my solution
# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def rangeSumBST(self, root, L: int, R: int) -> int:
        if not root:
            return 0
        summation = 0
        summation = self.traverse(root, summation, L, R)
        return summation

    def traverse(self, root, summation, L, R):
        if root:
            summation += self.visit(root.val, L, R)
            summation = self.traverse(root.left, summation, L, R)
            summation = self.traverse(root.right, summation, L, R)
        return summation

    def visit(self, value, L, R):
        if value >= L and value <= R:
            return value
        return 0