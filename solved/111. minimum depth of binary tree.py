# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        level = 0
        while queue:
            queue, level, flag = self.visit(queue, level)
            if flag:
                return level

    def visit(self, arr, l):
        l += 1
        children = []
        flag = False
        while arr:
            node = arr.pop(0)
            if self.is_leaf(node):
                flag = True
                return children, l, flag
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        return children, l, flag

    def is_leaf(self, n):
        if not n.left and not n.right:
            return True
        else:
            return False

# solution from leetcode
from collections import deque
class SolutionFast:
    def minDepth(self, root: TreeNode) -> int:
        result = []
        if root is None:
            return 0

        qeue = deque()
        qeue.append(root)
        j = 0
        while qeue:
            curr_length = len(qeue)
            current_level = []
            for i in range(curr_length):
                current_node = qeue.popleft()
                current_level.append(current_node.val)

                if current_node.left:
                    qeue.append(current_node.left)
                if current_node.right:
                    qeue.append(current_node.right)
                if current_node.left is None and current_node.right is None:
                    return j + 1
            result.append(current_level)
            j += 1

# solution from leetcode (recursive)
class SolutionRec:
    def minDepth(self, root: TreeNode) -> int:
        # bfs
        queue = deque()
        queue.append([root, 1])
        depth = float("inf")

        while len(queue) > 0:
            curr, lvl = queue.popleft()

            if curr is None:
                continue
            if curr.left is None and curr.right is None:
                return lvl

            queue.append([curr.left, lvl + 1])
            queue.append([curr.right, lvl + 1])

        return 0

# RECURSIVE
class SolutionRec2:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l and r:
            return 1 + min(l, r)
        else:
            return 1 + max(l, r)