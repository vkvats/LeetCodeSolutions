
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        while stack:
            stack = self.traverse(stack)
        return root

    def traverse(self, arr):
        children, parents = [], []
        while arr:
            node = arr.pop(0)
            parents.append(node)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

        for i in range(len(parents) - 1):
            n = parents[i]
            next_n = parents[i + 1]
            n.next = next_n
        return children

# in contant space
class SolutionF1:
    def connect(self, root: 'Node') -> 'Node':
        head = root

        while root:
            dummy = Node()
            pre = dummy

            while root:

                if root.left:
                    pre.next, pre = root.left, root.left

                if root.right:
                    pre.next, pre = root.right, root.right

                root = root.next

            root = dummy.next

        return head

# using deque
from collections import deque
class SolutionF2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque()
        queue.append(root)
        queue.append(None)

        while queue:
            current = queue.popleft()
            if not current:  # end of current level
                if queue:
                    queue.append(None)
            else:
                current.next = queue[0]

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return root