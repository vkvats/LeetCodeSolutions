# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        # Search for our target node "n"
        n,par = root, None # n is our target for deletion (after iterating), par is its parent node
        while n and n.val!=key: # Traverse... while n is valid, and it doesn't match the key
            par = n
            n   = n.left if key < n.val else n.right
        if not n:
            return root # Key not Found
        #
        # Deletion: 4 Main Cases
        if (not n.left) and (not n.right):
            # A) Leaf Detected. Delete 100%
            new = None
        elif not n.left:
            # B) Left Branch Empty. Keep Right Branch.
            new = n.right
        elif not n.right:
            # C) Right Branch Empty. Keep Left Branch.
            new = n.left
        else:
            # D) Both branches exist. Make Right Branch Official, and place n.left and its left-most side.
            new = n.right
            # Find left-most side of n.right
            n2 = new
            while n2.left:
                n2 = n2.left
            # Place n.left at the left of our "new" sub-tree
            n2.left = n.left
        #
        # Insertion: 3 Cases
        if not par:
            # A) root node was deleted, return "new" sub-tree
            return new
        if par.left == n:
            # B) Replace "par.left" with our "new" sub-tree.
            par.left = new
        else:
            # C) Replace "par.right" with our "new" sub-tree.
            par.right = new
        return root

# recurssive
class SolutionRec:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            temp = root.right
            mini = temp.val
            while temp.left:
                temp = temp.left
                mini = temp.val
            root.val = mini
            root.right = self.deleteNode(root.right,mini)
            return root
        return root

# Recursive 2
class SolutionRec2:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        if not root:
            return None

        if root.val == key:
            # find the smallest node in the right subtree

            if not root.left and not root.right:
                return None

            elif not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                temp = root.right

                if not temp.left:
                    temp.left = root.left
                    return temp

                else:

                    successor = temp.left

                    while successor.left:
                        temp = temp.left
                        successor = successor.left

                    temp.left = successor.right
                    successor.left = root.left
                    successor.right = root.right

                    return successor

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            root.left = self.deleteNode(root.left, key)

        return root