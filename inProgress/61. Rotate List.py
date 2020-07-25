# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        all_nodes = []
        node = head
        while node:
            all_nodes.append(node)
            node = node.next
        if len(all_nodes) <= 1: return head
        k = k % len(all_nodes)

        for _ in range(k):
            last_node = all_nodes.pop()
            second_last_node = all_nodes[-1]
            first_node = all_nodes[0]
            last_node.next = first_node
            second_last_node.next = None
            all_nodes.insert(0, last_node)
        return all_nodes[0]

# Solution from leetcode
# iterate till k value and then change the pointer only once
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #evaluate the length
        if not head:
            return
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        k %= length
        p = head
        for i in range(length-k-1):
            p = p.next
        newhead = p.next
        if not newhead:
            return head
        p.next = None
        cur.next = head
        return newhead