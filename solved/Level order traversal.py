# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root) -> [[int]]:
        if not root:
            return []
        queue = []
        output = []
        queue.append(root)
        while queue:
            queue, nodes = self.pop(queue)
            tmp_node_val = []
            while nodes:
                node = nodes.pop(0)
                tmp_node_val.append(node.val)
            output.append(tmp_node_val)
        return output

    def pop(self, queue):
        tmp_queue = []
        tmp_nodes = []
        while queue:
            node = queue.pop(0)
            tmp_nodes.append(node)
            if node.left:
                tmp_queue.append(node.left)
            if node.right:
                tmp_queue.append(node.right)
        return tmp_queue, tmp_nodes




