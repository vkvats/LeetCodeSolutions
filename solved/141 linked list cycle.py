# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        nodes = []
        while head.next != None:
            if head not in nodes:
                nodes.append(head)
                head = head.next
            else:
                return True
        return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        d = set()
        while head:
            if head in d:
                return True
            else:
                d.add(head)
            head = head.next
        return False