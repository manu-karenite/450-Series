#https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        getLevel=self.genLevel(root)
        if len(getLevel)==0:
            return None
        #print(getLevel)
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
       # print(ans)
        fin=[]
        for x in ans:
            fin.append(x[-1].val)
        print(fin)
        return fin
        
        