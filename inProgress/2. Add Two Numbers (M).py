# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1 = ""
        val2 = ""
        while l1 or l2:
            if l1:
                val1 += str(l1.val)
                l1 = l1.next

            if l2:
                val2 += str(l2.val)
                l2 = l2.next
        new_num = str(int(val1[::-1]) + int(val2[::-1]))[::-1]
        print(new_num)
        head = ListNode(int(new_num[0]))
        node = head
        count = 1
        while count < len(new_num):
            new = ListNode(new_num[count])
            node.next = new
            node = node.next
            count += 1
        return head

# Solution from leetcode (directly adding )
class SolutionF1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return dummy.next