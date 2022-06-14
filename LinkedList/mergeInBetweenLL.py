#https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        p=[]
        q=[]
        temp=list1
        while temp:
            p.append(temp.val)
            temp=temp.next
        
        temp=list2
        while temp:
            q.append(temp.val)
            temp=temp.next
        print(p,q)
        n=p[:a]+q+p[b+1:]
        print(n)
        
        l=[]
        for x in n:
            l.append(ListNode(x))
        for i  in range(0,len(n)-1):
            l[i].next=l[i+1]
        return l[0]
        
        