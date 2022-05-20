#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        st=""
        while temp is not None:
            st=st+str(temp.val)
            temp=temp.next
        
        print(st)
        #st=(st)
        st=st[::-1]
        print(st)
        
        i=0
        j=0
        l=len(st)
        sum=0
        while j<l:
            c=st[j:j+1]
            sum=sum+(2**i)*int(c)
            j=j+1
            i=i+1
        return(sum)
            
        