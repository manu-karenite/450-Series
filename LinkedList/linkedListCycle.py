#https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=set()
        temp=head
        while temp is not None:
            if temp in a:
                return True
            a.add(temp)
            temp=temp.next
        return False
            
        