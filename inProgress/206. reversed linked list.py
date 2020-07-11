# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        current_node =  head
        while current_node != None:
            next_temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_temp
        return prev_node

# fastest solution on leetcode
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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