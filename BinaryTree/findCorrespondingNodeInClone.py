#https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return None
        if cloned.val==target.val:
            return cloned
        
        #look for left or right
        ans=self.getTargetCopy(original,cloned.left,target)
        if ans:
            return ans
        return self.getTargetCopy(original,cloned.right,target)
        
        
    
        