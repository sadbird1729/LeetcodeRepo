# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:#必须有fast.next，不能只fast,也不能fast.next.next .如 [1] -1
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                idx1, idx2 = head, fast
                while idx1 != idx2:
                    idx1 = idx1.next
                    idx2 = idx2.next
                return idx1
        return None