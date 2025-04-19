# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive solution
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        self.tail = None
        self.start = None
        self.count = 1
        if n == 1 or m == n: return head

        def rev(node):
            if self.count == n:
                self.tail = node.next
                return (node, node)
            self.count += 1
            ret_node, rev_head = rev(node.next)
            ret_node.next = node
            node.next = None
            return node, rev_head

        root, prev = head, None
        while self.count < m:
            prev = root
            root = root.next
            self.count += 1
        n, rev_head = rev(root)
        n.next = self.tail
        if prev != None:
            prev.next = rev_head
        return rev_head if prev == None else head