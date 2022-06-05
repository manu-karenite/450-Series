#https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        lcheck=self.isUnivalTree(root.left)
        rcheck=self.isUnivalTree(root.right)
        
        currLeft=True
        if root.left:
            if root.left.val!=root.val:
                currLeft=False
        
        currRight=True
        if root.right:
            if root.right.val!=root.val:
                currRight=False
                
        return (lcheck and rcheck and currLeft and currRight)
        
        