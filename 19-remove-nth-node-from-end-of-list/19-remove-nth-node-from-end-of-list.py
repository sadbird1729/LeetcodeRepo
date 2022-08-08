# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        pre = dummy
        while n:
            pre = pre.next
            n -= 1
        cur = dummy
        while pre.next:
            pre = pre.next
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next
