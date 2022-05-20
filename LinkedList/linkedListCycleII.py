#https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=set()
        temp=head
        while temp is not None:
            
            if temp in a:
                return temp
            a.add(temp)
            temp=temp.next
        return None
        