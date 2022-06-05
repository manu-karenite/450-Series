#https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def leafList(self,root):
        if root is None:
            return []
        
        vec1=self.leafList(root.left)
        
        if root.left is None and root.right is None:
            vec1.append(root.val)
        
        vec2=self.leafList(root.right)
        
        vec1=vec1+vec2
        return vec1
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        lis1=self.leafList(root1)
        lis2=self.leafList(root2)
        return lis1==lis2
        