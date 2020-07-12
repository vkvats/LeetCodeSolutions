
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> [int]:
        output = []
        return self.traverse(root, output)

    # Recursive
    def traverse(self, node, output):
        if not node:
            return output
        if not node.children:
            output = output + [node.val]
            return output
        for child in node.children:
            output = self.traverse(child, output)
        output = output + [node.val]
        return output

        # iterative, reversed preorder traversal
    def postorderIterative(self, root):
        if root == None:
            return []

        stack, ans = [root], []

        while stack:
            # popping at '0', the first element to meet, i.e. root, should be the last element in array
            node = stack.pop(0)
            # inserting at index, 0, as the first element to insert should be the last element in post order.
            ans.insert(0, node.val)
            # since we are inserting at index, 0, we need to reverse the order of children to satisfy the
            # condition or ordered traversal.
            # node.children[::-1] need to inserted before stack so as to maintain the correct order.
            stack = node.children[::-1] + stack

        return ans


# from leet code (FAST)
class SolutionFast:
    def postorder(self, root: 'Node') -> [int]:

        output = []

        def recursive(root):
            if root:

                for i in root.children:
                    recursive(i)
                output.append(root.val)

        recursive(root)

        return output


# from leetcode fast 2
class SolutionFast2:
    def postorder(self, root: 'Node') -> [int]:
        self.result = []

        def traverse(root):
            if not root:
                return
            for child in root.children:
                traverse(child)
            self.result.append(root.val)

        traverse(root)
        return self.result


# from leetcode Iterative
class SolutionItr:
    def postorder(self, root: 'Node') -> [int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[:])

        return output[::-1]

