# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# New method
# recursive with nested function
class SolutionRecursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        def reverse(head):
            if not head.next:
                root = head
                return (head, root)
            else:
                node, root = reverse(head.next)
                node.next = head
                head.next = None
                return head, root

        node, root = reverse(head)
        node.next = None
        return root

# Iterative solution
class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # We need to return prev node as when
        # current node is None, prev node will become the head at the end.
        return prev


# fastest solution on leetcode
# With dummy node
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            head.next, dummy.next, head = dummy.next, head, head.next
        return dummy.next

    def recursiveReverse(self, head: ListNode):
        if head is None or head.next is None:
            return head, head

        next, tail = self.recursiveReverse(head.next)
        tail.next = head
        head.next = None

        return next, head