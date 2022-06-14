#https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p=[]
        q=[]
        temp=list1
        while temp:
            p.append(str(temp.val))
            temp=temp.next
        
        temp=list2
        while temp:
            q.append(str(temp.val))
            temp=temp.next
       
        p=int("".join(p))
        q=int("".join(q))
        print(p,q)
        s=list(str(p+q))
        print(s)
        
        temp=[]
        for x in s:
            temp.append(ListNode(int(x)))
        for i in range(0,len(s)-1):
            temp[i].next=temp[i+1]
        return temp[0]
            
        
        
        