# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        while headA or headB:
            if headA:
                if headA in nodes:
                    return headA
                else:
                    nodes.add(headA)
                    headA = headA.next
            if headB:
                if headB in nodes:
                    return headB
                else:
                    nodes.add(headB)
                    headB = headB.next
        return None
