# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        prev_node = None
        init_head = None
        while head.next != None:
            if head.val == val:
                if prev_node == None:
                    head = head.next
                else:
                    prev_node.next = head.next
                    head = head.next
            else:
                if init_head == None:
                    init_head = head
                prev_node = head
                head = head.next
        if head.val == val and init_head ==None:
            return None
        elif head.val == val and init_head != None:
            prev_node.next = head.next
            return init_head
        elif head.val != val and init_head == None:
            return head
        else:
            return init_head





# Solution from leetcode

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """Remove all occurences of val from the input list"""
        if head is None:
            return None

        tmp = head
        prev = None

        while tmp:
            if tmp.val == val:
                if prev is None:
                    head = tmp.next
                else:
                    prev.next = tmp.next
                tmp = tmp.next
                continue

            prev = tmp
            tmp = tmp.next

        return head


values = [1]#,2,6,3,4,5,6]
val = 1# [1,1,2,3,3]
linked_list = ListNode(values[0])
head = linked_list
for i in range(1, len(values)):
    new_node = ListNode(values[i])
    linked_list.next = new_node
    linked_list = linked_list.next
sol = Solution().removeElements(head, val)
# while sol.next != None:
#     print(sol.val)
#     sol = sol.next
# print(sol.val)