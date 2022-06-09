#https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        l=[]
        r=[]
        temp=head
        while temp:
            if temp.val<x:
                l.append(temp)
            else:
                r.append(temp)
            temp=temp.next
        curr=l+r
        print(curr)
        
        curr[-1].next=None
        i=0
        while i<len(curr)-1:
            curr[i].next=curr[i+1]
            i+=1
        return curr[0]