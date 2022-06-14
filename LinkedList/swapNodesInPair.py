#https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp)
            temp=temp.next
        print(ans)
        
        if len(ans)%2==0:
            for i in range(0,len(ans),2):
                temp=ans[i]
                ans[i]=ans[i+1]
                ans[i+1]=temp
            
            
            
        else:
            for i in range(0,len(ans)-1,2):
                temp=ans[i]
                ans[i]=ans[i+1]
                ans[i+1]=temp
        print(ans)
        for i in range(0,len(ans)-1):
            ans[i].next=ans[i+1]
        ans[-1].next=None
        return ans[0]
    
            