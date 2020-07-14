
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        stack = [root]
        level = 0
        while stack:
            stack, level = self.pop(stack, level)
        return level

    def pop(self, array, level):
        level += 1
        children = []
        while array:
            node = array.pop()
            if node.children:
                children = children + node.children

        return children, level

# solution from leetcode Fast
### Similar solution done inside only one function
class SolutionFast:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        stack = [root]
        count = 0
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if node:
                    if node.children:
                        stack.extend(node.children)
            count += 1

        return count

# solution from leetcode (Recursive)
class SolutionRecursive:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        def dfs(n):
            if n.children is None:
                return 1
            # this will keep track of max depth in DFS
            mdepth = 0
            for c in n.children:
                depth = 1 + dfs(c)
                mdepth = max(mdepth, depth)
            return mdepth
# we need to add 1 before final anser from insider function as
        # the function dfs() do not count the root level.
        return 1 + dfs(root)


# Solution from leetcode (recursive)
class SolutionRecurr2:
    def calcDepth(self, node,level):
            if not node:
                return 0
            self.answer = max(self.answer, level)
            for child in node.children:
                self.calcDepth(child, level+1)


    def maxDepth(self, root: 'Node') -> int:
        self.answer = 0
        self.calcDepth(root,1)
        return self.answer