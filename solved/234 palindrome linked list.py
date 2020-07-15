# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        nodes_val = []
        while head.next != None:
            nodes_val.append(head.val)
            head = head.next
        nodes_val.append(head.val)
        reversed_nodes_val = nodes_val[::-1]
        for i in range(len(nodes_val)):
            if reversed_nodes_val[i] != nodes_val[i]:
                return False
        return True


values = [1,2] # [1,1,2,3,3]
linked_list = ListNode(values[0])
head = linked_list
for i in range(1, len(values)):
    new_node = ListNode(values[i])
    linked_list.next = new_node
    linked_list = linked_list.next
sol = Solution().isPalindrome(head)
print(sol)