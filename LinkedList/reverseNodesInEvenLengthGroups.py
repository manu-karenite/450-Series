#https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp)
            temp=temp.next
        #rint(ans)
        
        fin=[]
        i=0
        k=1
        while i<len(ans):
            temp=ans[i:i+k]
            fin.append(temp)
            i=i+k
            k+=1
        #rint(fin)
        
        fin1=[]
        ct=1
        for i,x in enumerate(fin):
            if len(x)%2==0:
                fin1.append(x[::-1])
                ct+=2
            else:
                fin1.append(x)
        #rint(fin1)
        fin2=[]
        for x in fin1:
            fin2=fin2+x
        for i in range(0,len(fin2)-1):
            fin2[i].next=fin2[i+1]
        fin2[-1].next=None
        return fin2[0]