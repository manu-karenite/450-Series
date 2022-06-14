#https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp)
            temp=temp.next
        #rint(ans)
        
        fin=[]
        for i in range(0,len(ans),k):
            curr=ans[i:i+k][::-1]
            if len(curr)==k:
                fin=fin+ans[i:i+k][::-1]
            else:
                fin=fin+ans[i:i+k]
        #rint(fin)
        
        for i in range(0,len(fin)-1):
            fin[i].next=fin[i+1]
        fin[-1].next=None
        return fin[0]
        