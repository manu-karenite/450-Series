#https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def ans(self,root1,root2):
        if not root1 and not root2:
            return True
        
        
        if root1 and root2 and root1.val==root2.val:
            return self.ans(root1.left,root2.right) and self.ans(root1.right,root2.left)
        
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        ans=self.ans(root,root)
        return ans
            
        