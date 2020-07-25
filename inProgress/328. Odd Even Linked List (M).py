# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # get the count
        node = head
        N = 0
        while node:
            N += 1
            node = node.next
        if N <= 2: return head
        prev_odd = head
        odd_head = prev_odd
        prev_even = head.next
        even_head = prev_even
        node2 = head.next.next
        prev_even.next = None
        prev_odd.next = None
        for val in range(3, N + 1):
            if val % 2 == 1:
                prev_odd.next = node2
                prev_odd = prev_odd.next
                if node2.next:
                    node2 = node2.next
                prev_odd.next = None
            else:
                prev_even.next = node2
                prev_even = prev_even.next
                if node2.next:
                    node2 = node2.next
                prev_even.next = None
        prev_odd.next = even_head
        return odd_head

    # without counting all nodes and for loop
    def oddEvenList(self, head: ListNode) -> ListNode:
        # get the count
        node = head
        N = 0
        while node:
            N += 1
            node = node.next
            if N > 2: break
        if N <= 2: return head
        prev_odd = head
        odd_head = prev_odd
        prev_even = head.next
        even_head = prev_even
        node2 = head.next.next
        prev_even.next = None
        prev_odd.next = None
        val = 3
        while True:
            if val % 2 == 1:
                prev_odd.next = node2
                prev_odd = prev_odd.next
                if node2.next:
                    node2 = node2.next
                else:
                    node2 = None
                prev_odd.next = None
                val += 1
            else:
                prev_even.next = node2
                prev_even = prev_even.next
                if node2.next:
                    node2 = node2.next
                else:
                    node2 = None
                prev_even.next = None
                val += 1
            if not node2: break
        prev_odd.next = even_head
        return odd_head

# Solutions from leetcode
class SolutionF3:
    def oddEvenList(self, head: ListNode) -> ListNode:
        curr = head
        even_head = None
        even_curr = None

        while curr is not None:
            if even_head is None:
                even_head = curr.next
                even_curr = curr.next
            else:
                even_curr.next = curr.next
                even_curr = even_curr.next
            if curr.next is None:
                break
            if curr.next.next is None:
                break
            curr.next = curr.next.next
            curr = curr.next

        if curr is not None:
            curr.next = even_head
        return head

