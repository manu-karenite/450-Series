#https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        print(ans)
        
        temp=ans[k-1]
        ans[k-1]=ans[-k]
        ans[-k]=temp
        print(ans)
        
        fin=[]
        for x in ans:
            fin.append(ListNode(x))
            
        for i in range(0,len(fin)-1):
            fin[i].next=fin[i+1]
        return fin[0]
        