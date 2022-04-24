# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        a = set()

        temp = headA
        while temp is not None:
            a.add(id(temp))
            temp = temp.next

        temp = headB
        while temp is not None:
            if id(temp) in a:
                return temp
            temp = temp.next

        return None
