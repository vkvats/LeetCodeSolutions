##### My solution same as 530 ########

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root, vals, ans):
        if not root:
            return
        # in-order traversal and also maintaining the min difference at index 0 in ans.
        self.helper(root.left, vals, ans)
        if vals:
            ans[0] = min(ans[0], root.val - vals[-1])

        vals.append(root.val)
        self.helper(root.right, vals, ans)

    def minDiffInBST(self, root: TreeNode) -> int:
        # inorder traversal
        vals = []
        ans = [float('inf')]
        self.helper(root, vals, ans)
        return ans[0]

# solution from leetcode
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        diff = float('inf')
        s = []
        node = root
        last_val = None
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                tmp = s.pop()
                if last_val and abs(tmp.val - last_val) < diff:
                    diff = tmp.val - last_val
                last_val = tmp.val
                node = tmp.right
        return diff

# solution from leetcode
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        def helper(root):
            if not root:
                return
            nonlocal ans, prev
            # in-order traversal
            # left node call
            helper(root.left)
            # visit
            if not prev:
                prev = root
            else:
                ans = min(ans, root.val - prev.val)
                prev = root
            # right node call
            helper(root.right)

        ans = float('inf')
        prev = None
        helper(root)
        return ans

