# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_elements = self.left_preorder_rec(root.left)
        print(left_elements)
        right_elements = self.right_rev_preorder_rec(root.right)
        print(right_elements)
        return left_elements == right_elements

    def left_preorder_rec(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.left_preorder_rec(root.left)
            res = res + self.left_preorder_rec(root.right)
        else:
            res = res + [None]
        return res

    def right_rev_preorder_rec(self, root):
        res = []
        if root:
            res.append(root.val)
            res = res + self.right_rev_preorder_rec(root.right)
            res = res + self.right_rev_preorder_rec(root.left)
        else:
            res = res + [None]

        return res

# Solution from leetcode. (recursive)
class SolutionFast1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and \
                   self.isMirror(leftroot.left, rightroot.right) and \
                   self.isMirror(leftroot.right, rightroot.left)
        return leftroot == rightroot
