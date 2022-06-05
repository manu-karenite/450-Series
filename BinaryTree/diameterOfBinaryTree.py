#https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def height(self,root):
        if root is None:
            return 0
        
        l=self.height(root.left)
        r=self.height(root.right)
        return max(l,r)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        
        l=self.diameterOfBinaryTree(root.left)
        r=self.diameterOfBinaryTree(root.right)
        
        lh=self.height(root.left)
        rh=self.height(root.right)
        
        return max({l,r,lh+rh})
        
        
        