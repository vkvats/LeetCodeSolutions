
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

# solution From leetcode
class SolutionF1:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        pre = root
        cur = None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root

# solution from leetcode
import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            size = len(queue)

            for i in range(len(queue)):
                node = queue.popleft()
                size -= 1

                if size > 0:
                    node.next = queue[0]
                else:
                    node.next = None

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root