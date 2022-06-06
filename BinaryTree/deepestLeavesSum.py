#https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self,root):
        if root is None:
            return []
        
        q=[root,None]
        
        i=0
        while q:
            curr=q[i]
            
            if curr is not None:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            else:
                if len(q[i+1:])>=1:
                    q.append(None)
                else:
                    break
            i+=1
        
        val=[]
        temp=[]
        for z in q:
            if z is not None:
                temp.append(z.val)
            else:
                val.append(temp)
                temp=[]
        
        print(val)
        return val
            
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        level=self.levelOrder(root)
        print(level)
        
        x=level[-1]
        return sum(x)
        
        