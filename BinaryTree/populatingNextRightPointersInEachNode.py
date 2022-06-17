#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def genLevel(self,root):
        if root is None:
            return []
        
        
        
        q=[root,None]
        i=0
        while q:
            curr=q[i]
            
            if not curr:
                if len(q[i+1:])>=1:
                    q.append(None)
                else:
                    break
                
                
                
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            i+=1
        return q
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    
        getLevel=self.genLevel(root)
        if len(getLevel)==0:
            return None
        ans=[]
        temp=[]
        for x in getLevel:
            if x:
                temp.append(x)
            else:
                
                ans.append(temp)
                temp=[]
        
        if len(temp)>0:
            ans.append(temp)
        print(ans)
        
        for x in ans:
            for i in range(0,len(x)-1,1):
                x[i].next=x[i+1]
            x[-1].next=None
        
        return ans[0][0]

            
        