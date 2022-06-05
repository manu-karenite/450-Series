#https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        
        
        s=0
        if low<root.val:
            s+=self.rangeSumBST(root.left,low,high)
        if high>root.val:
            s+=self.rangeSumBST(root.right,low,high)
            
        if root.val>=low and root.val<=high:
            s+=root.val
        return s
            
            
        