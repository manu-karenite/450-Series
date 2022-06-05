#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def ans(self,root):
        if not root:
            return [[]]
        
        
        if root and not root.left and not root.right:
            return [[str(root.val)]]
        
        
        l=self.ans(root.left)
        r=self.ans(root.right)
        ans=[]
        if l:
            for x in l:
                if len(x)>0:
                    temp=x
                    temp.append(str(root.val))
                    ans.append(temp)
        
        if r:
            for x in r:
                if len(x)>0:
                    temp=x
                    temp.append(str(root.val))
                    ans.append(temp)
        return ans
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        t=self.ans(root)
        print(t)
        s=0
        for z in t:
            l="".join(z)
            l=l[::-1]
            l=int(l,2)
            s+=l
        return s
            
        