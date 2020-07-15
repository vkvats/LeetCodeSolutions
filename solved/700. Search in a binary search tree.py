# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        return self.traverse(root, val)

    def traverse(self, node, value):
        if node:
            if node.val == value:
                return node
            else:
                if node.val > value:
                    node = self.traverse(node.left, value)
                else:
                    node = self.traverse(node.right, value)
        return node


# solutions from leetcode
class SolutionFast:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        if val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)

class SolutionITR:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            print(curr.val)
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return curr
        return None

