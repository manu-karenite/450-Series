#https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #no not need
        if not head:
            return None
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        
        ans.sort()
        
        fin=[]
        for x in ans:
            fin.append(ListNode(x))
            
        for i in range(0,len(fin)-1):
            fin[i].next=fin[i+1]
        return fin[0]
        