# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        dummy = ListNode(-1)

        prev_node = dummy

        while node1 or node2:
            if not node1 or not node2:
                # break the loop if any one of the linked list
                # has reached its end, because all others are
                # already sorted and we just need to change the pointer
                break
            next_node = None
            if node1.val <= node2.val:
                next_node = node1
                node1 = next_node.next
            else:
                next_node = node2
                node2  = next_node.next
            prev_node.next = next_node
            prev_node = next_node
        prev_node.next = node1 or node2
        return dummy.next

# solution from leetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1
        node1 = l1
        node2 = l2
        newlist = ListNode(min(node1.val, node2.val))
        node = newlist
        if node1.val < node2.val: node1 = node1.next
        else: node2 = node2.next
        while node1 and node2:
            if node1.val > node2.val:
                node.next =  ListNode(node2.val)
                node = node.next
                node2 = node2.next
            else:
                node.next =  ListNode(node1.val)
                node = node.next
                node1 = node1.next
        if node1:
            node.next = node1
        elif node2:
            node.next = node2
        return newlist

val1 = [1,2, 3, 4, 5, 6]
val2 = [1, 2, 4, 7,8, 9, 10]
# val1 = [1, 3]
# val2 = [2, 4]
if len(val1) > 0 and len(val2) > 0:
    head1 = ListNode(val1[0])
    prev_node = head1
    for i in range(1, len(val1)):
        node = ListNode(val1[i])
        prev_node.next = node
        prev_node = node
    head2 = ListNode(val2[0])
    prev_node = head2
    for i in range(1, len(val2)):
        node = ListNode(val2[i])
        prev_node.next = node
        prev_node = node
    sol = Solution().mergeTwoLists(head1, head2)
    while sol:
        print(sol.val)
        sol = sol.next