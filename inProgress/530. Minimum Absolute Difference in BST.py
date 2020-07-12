# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        node_vals = []
        stack = [root]
        while stack:
            node = stack.pop()
            node_vals.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        node_vals.sort()
        d = []
        for i in range(0, len(node_vals) - 1):
            diff = abs(node_vals[i] - node_vals[i + 1])
            d.append(diff)
        return min(d)

# solution from leetcode (FAST)
class SolutionFast1:
    def getMinimumDifference(self, root: TreeNode) -> int:

        def dfs(node):
            if root:
                if node.left: dfs(node.left)
                final.append(node.val)
                if node.right: dfs(node.right)

        final = []
        dfs(root)
        return min(final[i] - final[i - 1] for i in range(1, len(final)))
# solution from leetcode (recursive)
class SolutionRecrsive:
    def getMinimumDifference(self, root: TreeNode) -> int:

        self.res = float('inf')
        self.prev = None

        def traverse(root: TreeNode) -> None:
            if not root:
                return None

            traverse(root.left)

            if self.prev is not None:
                self.res = min(root.val - self.prev, self.res)

            self.prev = root.val
            traverse(root.right)

        traverse(root)
        return self.res

# iterative solution
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        #         tmp = []
        #         while root:
        #             tmp.append(root.val)

        #             if root.left != None:
        #                 root = root.left

        #             else:
        #                 root = root.right
        #         res = tmp[0]

        #         for i in range(len(tmp)-1):
        #             res = min(abs(tmp[i+1]-tmp[i]),res)
        #             print(i,res,abs(tmp[i+1]-res))

        # return res

        prev, cur, res = -math.inf, None, math.inf
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            cur = node.val
            res = min(res, cur - prev)
            prev = cur
            root = node.right
        return res

# form leetcode
class Solution4:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack = []
        pre = -float('inf')
        result = float('inf')
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result = min(node.val - pre, result)
            pre = node.val
            root = node.right
