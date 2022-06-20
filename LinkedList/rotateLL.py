#https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            #print("ONE ELEMENT")
            return head
        
        a=[]
        temp=head
        ct=0
        while temp:
            a.append(temp)
            temp=temp.next
            ct+=1
        #print(a)
        
        k=k%ct
        #print(ct)
        fin=[]
        if k==0:
            fin=a[0:ct]
            #print(fin)
        else:
            
            # print(a[-k:])
            # print(a[:ct-k])
            fin=a[-k:]+a[:ct-k]
            #print(fin)
        
        for i in range(0,ct-1,1):
            fin[i].next=fin[i+1]
        fin[-1].next=None
        return fin[0]