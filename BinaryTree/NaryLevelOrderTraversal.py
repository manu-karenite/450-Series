#https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def level(self,root):
        if not root:
            return []
        
        if len(root.children)==0:
            return [[root.val]]
        
        
        q=[root,None]
        i=0
        while q:
            curr=q[i]
            if curr is None:
                
                if len(q[i+1:])>=1:
                    #insert None
                    q.append(None)
                    
                else:
                    break
                
                
                
                
                
            else:
                #insert its children to q
                for x in curr.children:
                    q.append(x)
            i+=1
        
        
        temp=[]
        fin=[]
        for x in q:
            if x is not None:
                temp.append(x.val)
                
            else:
                fin.append(temp)
                temp=[]
        return fin
    
    
        
        
        
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        
        mgList=self.level(root)
        return(mgList)
        
        
        