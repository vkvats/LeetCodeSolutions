# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        stack = [root]
        while stack:
            stack, cousin = self.traverse(stack, x, y)
            if cousin: return cousin
        return False

    def traverse(self, arr, x, y):
        children = set()
        x_parent, y_parent = 0, 0
        while arr:
            node = arr.pop()
            if node.left:
                if node.left.val == x:
                    x_parent = node.val
                if node.left.val == y:
                    y_parent = node.val
                children.add(node.left)
            if node.right:
                if node.right.val == x:
                    x_parent = node.val
                if node.right.val == y:
                    y_parent = node.val
                children.add(node.right)
        cousin = False
        if (x_parent and y_parent) and (x_parent != y_parent):
            cousin = True
        return list(children), cousin

#  solutions from leetcode
import collections
class SolutionFast1:
	def isCousins(self, root, x, y):
		nodes = collections.defaultdict(list)
		queue = [(root,0,0)]
		while queue:
			node,level,parent = queue.pop(0)
			nodes[node.val] = [level,parent]

			if node.left:
				queue.append((node.left,level+1,node.val))
			if node.right:
				queue.append((node.right,level+1,node.val))

		if nodes[x][0]==nodes[y][0] and nodes[x][1] != nodes[y][1]:
			return True

		return False

# Solution from leetcode (DFS)
class SolutionDFS:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        results = []
        self.dfs(root, None, 0, results, x, y)
        return results[0][0] != results[1][0] and results[0][1] == results[1][1]

    def dfs(self, node, parent, depth, results, x, y):
        if node and len(results) != 2:
            if node.val == x or node.val == y:
                results.append((parent, depth))
            self.dfs(node.left, node, depth + 1, results, x, y)
            self.dfs(node.right, node, depth + 1, results, x, y)
