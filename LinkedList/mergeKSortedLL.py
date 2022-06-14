#https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        
        ans=[]
        for x in lists:
            if x is None:
                continue
            
            temp=x
            while temp:
                ans.append(temp.val)
                temp=temp.next
            
        print(ans)
        if len(ans)==0:
            return None
        
        ans.sort()
        print(ans)
        
        temp=[]
        for x in ans:
            node=ListNode(x)
            temp.append(node)
        print(temp)
        
        for i in range(0,len(temp)-1):
            temp[i].next=temp[i+1]
        return temp[0]
            
        