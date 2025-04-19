# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> [int]:
        if not root:
            return root
        count = {}
        stack = [root]
        most_count = -10
        while stack:
            node = stack.pop()
            f = count.get(node.val, 0) + 1
            count[node.val] = f
            if f > most_count:
                most_count = f
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        output = []
        for key, value in count.items():
            if most_count == value:
                output.append(key)
        return output

# Solution from leetcode.
