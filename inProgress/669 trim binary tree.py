# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def dfs(node):
            if node is None: return None
            # traversing using properties of tree
            if node.val < L: return dfs(node.right)
            elif node.val > R: return dfs(node.left)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        return dfs(root)


        # Non-recursive
        ret = TreeNode()
        stack = [(root, (ret, 'l'))]
        while stack:
            node, (p, dir) = stack.pop()

            if node is None: continue
            if node.val < L:
                if dir == 'l':
                    p.left = None
                else:
                    p.right = None
                stack.append((node.right, (p, dir)))
                continue
            elif node.val > R:
                if dir == 'l':
                    p.left = None
                else:
                    p.right = None
                stack.append((node.left, (p, dir)))
                continue
            else:
                if dir == 'l':
                    p.left = node
                else:
                    p.right = node

            stack.append((node.right, (node, 'r')))
            stack.append((node.left, (node, 'l')))

        return ret.left


# solution from leetcode
class SolutionFast1:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        lower = L
        upper = R
        def recur(node):
            if not node:
                return None
            if node.val > upper:
                return recur(node.left)
            if node.val < lower:
                return recur(node.right)
            L = recur(node.left)
            R = recur(node.right)
            node.left = L
            node.right = R
            return node
        return recur(root)


# solution from leetcode
class SolutionFast2:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root: return None
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            return self.trimBST(root.left, L, R)

