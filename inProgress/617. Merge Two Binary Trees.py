#### MY SOLUTION ####
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Insert Node
    def insert(self, val):

        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

# solution from discussion
class SolutionDiscussion:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            if t1: return t1
            if t2: return t2
            return None
        return TreeNode(t1.val + t2.val, self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right))

# Leetcode fast solution (making new tree)
class SolutionFast:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # Recursive
        def solve(t1: TreeNode, t2: TreeNode) -> TreeNode:
            if not t1 and not t2:
                return None

            elif not t1:
                return t2

            elif not t2:
                return t1

            else:
                root = TreeNode(t1.val + t2.val)
                root.left = solve(t1.left, t2.left)
                root.right = solve(t1.right, t2.right)
                return root

        return solve(t1, t2)

### IN PLACE SOLUTION ###
class SolutionInplace:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1








if __name__ == '__main__':
    values1 = [1,2,3,5]
    values2 = [2,1,3,4,7]
    t1 = TreeNode(values1[0])
    t2 = TreeNode(values2[0])
    for i in range(1, len(values1)):
        t1.insert(values1[i])
    for i in range(1, len(values2)):
        t2.insert(values2[i])
    sol = Solution().mergeTrees(t1, t2)
    def inorderTraversal(root):
        res = []
        if root:
            res = inorderTraversal(root.left)
            res.append(root.val)
            res = res + inorderTraversal(root.right)
        return res
    print(inorderTraversal(sol))
