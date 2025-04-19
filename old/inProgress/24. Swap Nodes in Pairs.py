# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # if there is no node or only one node, return head as it is.
        if not head or not head.next: return head
        # else, linked list has 2 or more nodes,
        # which can be classified into two groups,
        # either odd number of nodes of even.
        tmp = head.next.next
        head, head.next = head.next, head
        # set it to none, and at the end, join the returned linked list to this.
        head.next.next = None
        # function to swap nodes, recursively
        def swap(head):
            # if not head, return
            if not head: return
            # if only one node left, return the node
            # which will be linked at the end.
            if not head.next:
                return head
            # for next two nodes, we need to swap
            tmp = head.next.next
            # swap
            head, head.next = head.next, head
            # set the link to none, add later
            head.next.next = None
            # recurse to swap
            node = swap(tmp)
            # add the node here
            head.next.next = node
            # return the head.
            return head
        # the head will be returned here.
        node =  swap(tmp)
        # add head to initial swapped head
        head.next.next = node
        return head

# iterative
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        tmp = head.next.next
        head, head.next = head.next, head
        prev = head.next
        head.next.next = None
        while tmp:
            node = tmp
            if not node.next:
                prev.next = node
                break
            tmp = node.next.next
            node, node.next = node.next, node
            node.next.next = None
            prev.next = node
            prev = node.next
        return head

# solutions from leetcode
# Iteratively sing dummy node.
# dummy node is not really required
def swapPairs1(self, head):
    dummy = p = ListNode(0)
    dummy.next = head
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        p.next = tmp
        head = head.next
        p = tmp.next
    return dummy.next


# Recursively ( a bit confusing)
def swapPairs(self, head):
    if head and head.next:
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head