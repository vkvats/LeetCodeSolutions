# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Iterative
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> [int]:
        if not root:
            return
        queue = [root]
        output = []
        while queue:
            queue, elements = self.visit(queue)
            output.append(elements)
        return output[::-1]

    def visit(self, que):
        parents, children = [], []
        while que:
            node = que.pop(0)
            parents.append(node.val)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        return children, parents

# Solution from leetcode (fast)
class SolutionFast1:
    def levelOrderBottom(self, root: TreeNode) :
        if root is None: return []
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res

    def levelOrderBottom(self, root: TreeNode) ->[int]:
        if root is None: return []
        res = []
        return self.bfs(root, 0, res)

    def bfs(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.bfs(root.left, level+1, res)
            self.bfs(root.right, level+1, res)
        return res

# Solution from leetcode (fast 2) (iterative)
class SolutionFast2:
    def levelOrderBottom(self, root: TreeNode) :

        if not root:
            return []

        queue = [root]
        ans = []

        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.insert(0, temp)

        return ans

# solution from leetcode (iterative)
class Solution3:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.insert(0, [node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans