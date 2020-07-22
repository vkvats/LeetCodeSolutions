# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return
        traversed = []
        flag = True
        stack = [head]
        while flag:
            node = stack.pop()
            if node in traversed:
                return node
            else:
                traversed.append(node)
            if node.next:
                stack.append(node.next)
            else: return None

# Solution without using Stack
class SolutionM2:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return
        traversed = {}
        flag = True
        node = head
        while flag:
            if node in traversed:
                return node
            else:
                traversed[node] = 1
            if node.next:
                node = node.next
            else: return None

# Solution from leetcode
class SolutionF1:

    def helper(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        pointer = self.helper(head)
        if pointer is None:
            return None

        ptr1 = pointer
        ptr2 = head

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

# Solution with additional details
class SolutionDetailed:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        # determine one of the nodes within the cycle
        slow, fast = head, head.next
        while True:
            if slow is fast:
                break
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next

        # determine the length of the cycle
        cur = slow.next
        cycle_len = 1
        while cur is not slow:
            cur = cur.next
            cycle_len += 1

        # iterate from beginning for length of cycle
        lead = head
        for _ in range(cycle_len):
            lead = lead.next

        # iterate both leading pointer and lagging pointer until they meet
        lag = head
        while lag is not lead:
            lag = lag.next
            lead = lead.next

        # where they meet is the cycle
        return lag