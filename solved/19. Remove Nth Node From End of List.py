# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        del_pos = length - n
        node2 = head
        if del_pos == 0:
            return head.next
        while node2:
            del_pos -= 1
            if del_pos == 0:
                node2.next = node2.next.next
            else:
                node2 = node2.next
        return head

# Solution from leetcode (Two pointer solution)
class SolutionTwoPointer:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Use runner method, 2 pointers
        # The fast one is n positions in front
        # When it reaches the end, the slow one is at position length-n, remove that node

        slow = fast = head
        for _ in range(n):
            fast = fast.next

        # Special case, n=1, len(list)=1, just return head.next
        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the item at slow pointer
        slow.next = slow.next.next

        return head
