#https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        l=[]
        r=[]
        
        ct=0
        temp=head
        while temp:
            if ct%2==0:
                l.append(temp)
            else:
                r.append(temp)
            temp=temp.next
            ct+=1
        #print(l,r)
        fin=l+r
        if len(fin)==0:
            return None
            
        for i in range(0,len(fin)-1):
            fin[i].next=fin[i+1]
        fin[-1].next=None
        return fin[0]
            
        