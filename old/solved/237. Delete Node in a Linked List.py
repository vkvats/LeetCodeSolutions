# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        The problem gives direct access to the node, so we don't need to traverse till the node
        and then do the pointer changes, we can directly change the pointer as we already
        have the access to the node.
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    values = [4,5,1,9]
    node = 5
    head = ListNode(values[0])
    prev_node = head
    for i in range(1, len(values)):

        node = ListNode(values[i])
        prev_node.next = node
        prev_node = prev_node.next
    sol = Solution().deleteNode(node)