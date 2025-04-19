### Time limit exceeded ###
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import numpy as np


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        node_val = []
        while stack:
            node = stack.pop()
            node_val.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        node_val = np.array(node_val)
        # convert to greate BST
        stack2 = [root]
        while stack2:
            node2 = stack2.pop()
            value = sum(node_val[node_val > node2.val])
            # print(value)
            node2.val = node2.val + value
            if node2.left:
                stack2.append(node2.left)
            if node2.right:
                stack2.append(node2.right)
        return root

## solution from solution (recursive)
class SolutionDiscussion:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

# Solution form discussion (Iterative)
class SolutionIterative:
    def convertBST(self, root):
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root

## Approach #3 Reverse Morris In-order Traversal [Accepted]
class SolutionMorris:
    def convertBST(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root

# solution from leetcode
class SolutionFast:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        node = root
        stack = []
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left
        return root

# Solution from leetcode
class SolutionFast2:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            """
            # traversing in right-> node -> left order.(reverse of in-order)
            
            If we go from right-> node -> left, then we can keep adding values
            and replace node.val with that value.
            """
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root