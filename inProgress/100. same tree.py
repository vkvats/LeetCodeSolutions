# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        stack1, stack2 = [p], [q]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1.val != node2.val:
                return False
            if node1.left and not node2.left:
                return False
            if node1.right and not node2.right:
                return False
            if not node1.left and node2.left:
                return False
            if not node1.right and node2.right:
                return False
            if node1.left:
                stack1.append(node1.left)
            if node1.right:
                stack1.append(node1.right)
            if node2.left:
                stack2.append(node2.left)
            if node2.right:
                stack2.append(node2.right)
        if (stack1 and not stack2) or (not stack1 and stack2):
            return False
        else:
            return True

# solution from leetcode (Recursive)
class SolutionFast1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

# solution from leetcode (recursive)
class SolutionFast2:
    def __init__(self):
        self.l = []

    def preorder(self, root):
        if root != None:
            self.l.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
        else:
            self.l.append(None)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        self.preorder(p)
        l1 = self.l[:]
        self.l = []
        self.preorder(q)
        l2 = self.l[:]
        self.l = []
        if l1 == l2:
            return True
        else:
            return False

# solution from leetcode( iterative)
from collections import deque
class SolutionItr:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if (not p) and (not q): return True
        if (not p) or (not q): return False

        queue = deque([(p, q)])

        while queue:
            p, q = queue.popleft()

            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            queue.append((p.left, q.left))
            queue.append((p.right, q.right))

        return True