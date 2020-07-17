# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        in_order_val = self.inorder(root)
        print(in_order_val)
        # create tree
        new_root = TreeNode(in_order_val[0])
        head = new_root
        for i in range(1, len(in_order_val)):
            n = TreeNode(in_order_val[i])
            new_root.right = n
            new_root = new_root.right
        return head

    def inorder(self, node):
        values = []
        if node:
            values = self.inorder(node.left)
            values.append(node.val)
            values = values + self.inorder(node.right)
        return values

# Solutions from leetcode
class SolutionFast:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.stack = []
        self.recurse(root)
        for i in range(len(self.stack)):
            self.stack[i].left = None
            if i + 1 == len(self.stack):
                self.stack[i].right = None
            else:
                self.stack[i].right = self.stack[i + 1]
        return self.stack[0]

    def recurse(self, node):
        if node.left:
            self.recurse(node.left)
        self.stack.append(node)
        if node.right:
            self.recurse(node.right)

# Solution from leetcode
class SolutionFast2:
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res