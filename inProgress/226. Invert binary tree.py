# My solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        # Precaution: we do not need to do any changes in the root.
        """
        # The whole While loop can be reduced to three line of code 
        It is because, we just need to invert, independednt of what is the 
        value of node.left and node.right.
        while stack:
            node = stack.pop()
            # visit : inversion
            node.left, node.right = node.right, node.left
            # insert node for next iteration
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)        
        return root
        """
        while stack:
            node = stack.pop()
            # tree inversion process
            if node.left and node.right:
                # append the node for next iteration
                stack.append(node.left)
                stack.append(node.right)
                # swap nodes/ inversion process
                node.left, node.right = node.right, node.left
            elif node.left and not node.right:
                # append the node for next iteration
                stack.append(node.left)
                # inversion process
                node.right = node.left
                node.left = None
            elif not node.left and node.right:
                # append the node for next iteration
                stack.append(node.right)
                # Inversion process.
                node.left = node.right
                node.right = None
        return root


# Solution from leetcode (Recursive)
class SolutionFast1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invertHelper(root)

        return root

    def invertHelper(self, node):
        # Base Case
        if node is None:
            return
        # Visit: Inversion step
        node.right, node.left = node.left, node.right
        # recursive Call
        self.invertHelper(node.left)
        self.invertHelper(node.right)

# solution from leetcode (recursive)
class SolutionFast2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        # combining even the Inversion step and recusive call.
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# 
