# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return  # return if only one head
        elif not head.next:
            return head  # return if only one node
        elif not head.next.next:
            return head  # return if only two nodes
        # reversing the nodes will start from three nodes.
        slow, fast = head, head
        while True:
            slow = slow.next
            fast = fast.next.next
            if fast.next == None:
                break
            elif fast.next.next == None:
                break
        # reverse all nodes from slow.next
        rev_head = self.reverse(slow.next)
        root = head  # 1
        if not rev_head: print("no head")
        while rev_head.next != None:
            tmp_root = root.next  # 2
            tmp_rev = rev_head.next  # 4
            root.next = rev_head
            rev_head.next = tmp_root
            root = tmp_root
            rev_head = tmp_rev
        # if there is reverse_head, that means
        # last exchange of node is remaining.
        if rev_head:
            tmp_root = root.next
            root.next = rev_head
            rev_head.next = tmp_root
            tmp_root.next = None
        return head

    def reverse(self, n: ListNode) -> ListNode:
        if not n or not n.next: return n

        def rev(n):
            if not n.next:
                root = n
                return (n, root)
            else:
                node, root = rev(n.next)
                node.next = n
                n.next = None
                return n, root

        node, root = rev(n)
        node.next = None
        return root

# A concise version
def reorderList(self, head):
    if not head:
        return

    # find the mid point
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half in-place
    pre, node = None, slow
    while node:
        pre, node.next, node = node, pre, node.next

    # Merge in-place; Note : the last node of "first" and "second" are the same
    first, second = head, pre
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    return













