#https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        lDone=self.invertTree(root.left)
        rDone=self.invertTree(root.right)
        
        #now just swap
        temp=lDone
        root.left=rDone
        root.right=temp
        return root
        