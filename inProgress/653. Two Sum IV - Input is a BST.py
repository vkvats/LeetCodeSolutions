# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        """
        This question needs two iteration, first iteration to generate the value to 
        be searched in the tree, and the second iteration through tree to actually 
        search the generated value. 
        Precaution: the node returned after search should not be same node 
        which was used to generate the search value in first place.
        """
        while stack:
            node = stack.pop()
            search_val = k - node.val
            out, out_val = self.search(root, search_val)
            if out and out_val != node:
                return out
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def search(self, head, value):
        stack = [head]
        while stack:
            node = stack.pop()
            # visit
            if node.val == value:
                return True, node
            # adding nodes using tree property
            # we should only search where we can actualy find the value.
            if node.left and node.val > value:
                stack.append(node.left)
            if node.right and node.val < value:
                stack.append(node.right)
        n = TreeNode(float('inf'))
        return False, n

# Solution from leetCode (iterative solution: just using set to reduce the time)
class SolutionFast:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # s maintains the value of nodes. It will reduce the time
        # of repeated search.
        s = set()
        bfs = [root]

        for i in bfs:
            if k - i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False

# solution from leetcode (Iterative: fundamentally same as above)
class SolutionFast2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return
        # using hashing to reduce the lookup time.
        hash1 = {}
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                if k - root.val in hash1:
                    return True
                hash1[root.val] = 0
                root = root.left
            root = stack.pop().right
        return False

# Solution from leetcode
class SolutionSol3:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        myset = set()
        def dfs(node):
            # base case: last case
            if not node:
                return False
            # visit: checking presence of value in set.
            if node.val in myset:
                return True
            # if not present, add the value to the set.
            myset.add(k - node.val)
            # recursive call
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
