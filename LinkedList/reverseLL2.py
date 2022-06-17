#https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
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
        a=a[:left-1]+a[left-1:right][::-1]+a[right:]
        #print(a)
        for i in range(0,ct-1,1):
            a[i].next=a[i+1]
        a[-1].next=None
        return a[0]
        