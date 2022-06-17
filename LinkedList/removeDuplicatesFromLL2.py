#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        
        d={}
        temp=head
        while temp:
            if temp.val in d:
                d[temp.val]+=1
            else:
                d[temp.val]=1
            temp=temp.next
        #print(d)
        s=set()
        for x in d:
            if d[x]==1:
                s.add(x)
        #print(s)
        
        temp=head
        a=[]
        while temp:
            if temp.val in s:
                a.append(temp)
            temp=temp.next
        
        
        if len(a)==0:
            return None
        for i in range(0,len(a)-1,1):
            a[i].next=a[i+1]
        a[-1].next=None
        return a[0]
            
                