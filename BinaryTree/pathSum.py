#https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def ans(self,root):
        if root is None:
            return [[]]
        
        if root is not None and root.left is None and root.right is None:
            return [[root.val]]
        
        
        vec1=self.ans(root.left)
        vec2=self.ans(root.right)
        
        ans=[]
        for x in vec1:
            if len(x)>0:
                temp=x
                temp.append(root.val)
                ans.append(temp)
        for x in vec2:
            if len(x)>0:
                temp=x
                temp.append(root.val)
                ans.append(temp)
        return ans
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        lis=self.ans(root)
        print(lis)
        for x in lis:
            if len(x)>0:
                s=sum(x)

                if s==targetSum:
                    return True
        return False
        