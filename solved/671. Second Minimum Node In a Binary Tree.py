# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        stack = [root]
        values = set()
        while stack:
            node = stack.pop(0)
            # values.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            values.add(node.val)
        if len(values) < 2:
            return -1
        else:

            return sorted(list(values))[1]

# Solution from leetCode
class SolutionFast1:
    def findSecondMinimumValue(self, root: TreeNode) -> int:

        if not root:
            return -1

        # dfs until we find the first value that differs from root.val
        # find minimum of all these values

        minimum = float('inf')

        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue

            if node.val > root.val:
                minimum = min(minimum, node.val)
                continue

            stack.append(node.left)
            stack.append(node.right)

        # def dfs(node):
        #    nonlocal minimum
        #    if not node:
        #        return

        #    if node.val > root.val:
        #        minimum = min(minimum, node.val)
        #        return

        #    dfs(node.left)
        #    dfs(node.right)
        # dfs(root)

        # Worst case: O(n)
        # Space complexity (stack): up to O(n)
        return -1 if minimum == float('inf') else minimum

# leetcode
class SolutionF2:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        uniques = set()

        def dfs(node):
            if node is None:
                return
            uniques.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        min1, ans = root.val, float('inf')

        for v in uniques:
            if min1 < v < ans:
                ans = v

        return ans if ans < float('inf') else -1