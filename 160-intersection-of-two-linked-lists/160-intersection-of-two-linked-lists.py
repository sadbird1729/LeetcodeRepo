# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        # A,B一起走，要么在相交点处相遇，要么在NULL处相遇
        # A走到头就从B开头走，B走到头就从A开头走
        # 设c为公共部分，A走了a+c+b+c，B走了b+c+a+c
        while A != B:
            if not A:
                A = headB
            else:
                A = A.next
            if not B:
                B = headA
            else:
                B = B.next
        return A 
