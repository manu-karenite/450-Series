#https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        #print(ans)
        
        fin=[]
        
        start=0
        end=0
        temp=[]
        while end<len(ans):
            if ans[end]!=0:
                temp.append(ans[end])
                end+=1
            else:
                #mil gaya 0
                fin.append(temp)
                temp=[]
                start=end+1
                end+=1
        #print(fin)
        
        fin=list(filter(lambda x: len(x)>0,fin))
        #print(fin)
        p=[]
        for x in fin:
            p.append(sum(x))
        q=[]
        for x in p:
            q.append(ListNode(x))
        #print(q)
        
        i=0
        while i<len(q)-1:
            q[i].next=q[i+1]
            i+=1
        return q[0]
            
            
        
        