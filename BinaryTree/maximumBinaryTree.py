#https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        
        foundMaxi=max(set(nums))
        #print(foundMaxi)
        idx=nums.index(foundMaxi)
        #print(idx)
        
        root=TreeNode(foundMaxi)
        l=self.constructMaximumBinaryTree(nums[:idx])
        r=self.constructMaximumBinaryTree(nums[idx+1:])
        root.left=l
        root.right=r
        return root
        