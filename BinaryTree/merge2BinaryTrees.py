#https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #lets keep root 1 as the original version
        
        if root1 is None and root2 is None: #00
            return None
        
        if not root1:
            return root2
        if not root2:
            return root1
        
        fromLeft=self.mergeTrees(root1.left,root2.left)
        fromRight=self.mergeTrees(root1.right,root2.right)
        
        
        if root1 is None and root2 is not None: #01
            
            root2.left=fromLeft
            root2.right=fromRight
            
            
        elif root1 is not None and root2 is None: #10
            root1.left=fromLeft
            root1.right=fromRight
            return root1
            
        elif root1 and root2: #11
            root1.val+=root2.val
            root1.left=fromLeft
            root1.right=fromRight
            return root1
            
        
#         if fromLeft is not None and fromRight is None: #10
#             root1.val+=root2.val
#             root1.left=fromLeft
#             root1.right=None
#             return root1
            
            
#         elif fromLeft is not None and fromRight is not None: #11
#             if root2:
#                 root1.val+=root2.val
#             root1.left=fromLeft
#             root1.right=fromRight
#             return root1
            
#         elif fromLeft is None and fromRight is not None: #01
#             if root2:
#                 root1.val+=root2.val
#             root1.left=None
#             root1.right=fromRight
#             return root1
            
#         elif fromLeft is None and fromRight is None: #00
#             if root2:
#                 root1.val+=root2.val
#             root1.left=root1.right=None