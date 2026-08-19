# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev= None
        curr = head
        while curr:
            next_node = curr.next  # Don't lose the rest
            curr.next = prev       # Reverse the arrow
            prev = curr            # Move reversed part forward
            curr = next_node       # Move to next node
        return prev