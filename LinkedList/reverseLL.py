#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next is None:
            return head
        
        n=self.reverseList(head.next)
        temp=n
        
        while temp.next is not None:
            temp=temp.next
        
        temp.next=head
        temp=temp.next
        temp.next=None
        return n
            