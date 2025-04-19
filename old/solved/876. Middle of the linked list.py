# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # temp = [head]
        #
        # while temp[-1].next:
        #     temp.append(temp[-1].next)
        #
        # return temp[len(temp) // 2]

        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow

        ### problem with output type
        size = 0
        current_node = head
        while head:
            size += 1
            head = head.next
        middle = size//2
        current_index = 0
        output = []
        while current_node:
            if current_index == middle:
                output.append(current_node.next)
            current_node = current_node.next
            current_index += 1
        return output

values = [1,2,3,4,5]
head = ListNode(values[0])
prev_node = head
for i in range(1, len(values)):
    node = ListNode(values[i])
    prev_node.next = node
    prev_node = prev_node.next

sol = Solution().middleNode(head)
print(sol)