#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        lis=[]
        temp=head
        while temp is not None:
            lis.append(temp.val)
            temp=temp.next
        print(lis)
        
        cap=len(lis)//2
        first=lis[0:cap]
        last=lis[cap:]
        last=last[::-1]
        
        i=0
        m=-2**31
        while i<len(first):
            m=max(m,first[i]+last[i])
            i=i+1
        return m
            
        