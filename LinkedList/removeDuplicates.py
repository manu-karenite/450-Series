#https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        orig=head
        n=self.deleteDuplicates(orig.next)
        if head.val==n.val:
            return n
        else:
            orig.next=None
            orig.next=n
            return orig
    
            
            
    
    
    
    