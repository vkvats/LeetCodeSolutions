# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        init_head = head
        cur_head = head
        while cur_head.next != None:
            next_node = cur_head.next
            if cur_head.val == next_node.val:
                cur_head.next = next_node.next
            else:
                cur_head = cur_head.next
        return init_head

# fast solution from leetcode
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # fast=slow=ListNode(0)
        fast = slow = head
        stack = []
        # print("")

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            top = stack.pop()
            if top != slow.val:
                return False
            slow = slow.next
        return True
    

values = [] # [1,1,2,3,3]
linked_list = ListNode(values[0])
head = linked_list
for i in range(1, len(values)):
    new_node = ListNode(values[i])
    linked_list.next = new_node
    linked_list = linked_list.next
sol = Solution().deleteDuplicates(head)
while sol.next != None:
    print(sol.val)
    sol = sol.next
print(sol.val)