#https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        
        #get the first Node as root
        root=TreeNode(nums[0])
        
        left1=[]
        right1=[]
        for x in nums[1:]:
            if x<root.val:
                left1.append(x)
            else:
                right1.append(x)
        
        l=self.bstFromPreorder(left1)
        r=self.bstFromPreorder(right1)
        root.left=l
        root.right=r
        return root
        