#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        temp=list1
        while temp:
            ans.append(temp.val)
            temp=temp.next
        temp=list2
        while temp:
            ans.append(temp.val)
            temp=temp.next
        print(ans)
        if len(ans)==0:
            return None
        
        ans.sort()
        fin=[]
        for x in ans:
            fin.append(ListNode(x))
        print(fin)
        
        for i in range(0,len(fin)-1):
            fin[i].next=fin[i+1]
        return fin[0]