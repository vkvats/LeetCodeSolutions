
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> [int]:
        output = []
        return self.traverse(root, output)

    def traverse(self, node, output):
        if not node:
            return output
        if not node.children:
            output = output + [node.val]
            return output
        if node:
            output = output + [node.val]
        for child in node.children:
            output = self.traverse(child, output)
        return output

#from leetcode Fast
class SolutionFast:
    def preorderChildren(self, children: ['Node'], arr: [int]):
        for i in children:
            arr.append(i.val)
            self.preorderChildren(i.children, arr)

    def preorder(self, root: 'Node') -> [int]:
        pre = []
        if root is not None:
            pre.append(root.val)
            self.preorderChildren(root.children, pre)
        return pre


# from leetcode fast 2
class SolutionFast2:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        L = []
        stack = [root]
        while len(stack):
            temp = stack.pop(-1)
            L.append(temp.val)

            for child in temp.children[::-1]:
                stack.append(child)

        return L
#recursive
        # L = []
        # def rec(root):
        #     if not root:
        #         return
        #     L.append(root.val)
        #     for child in root.children:
        #         rec(child)
        #
        # rec(root)
        # return L

#from leetcode (recursive)
class SolutionRecursive:
    def preorder(self, root: 'Node') -> [int]:
        res = []
        self._preorder(root, res)
        return res

    def _preorder(self, root: 'Node', res: [int]):
        if not root:
            return

        res.append(root.val)
        if root.children:
            for child in root.children:
                self._preorder(child, res)
