#https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfNodes(self,root):
        #return [sum,count]
        if root is None:
            return [0,0]
        
        x=self.sumOfNodes(root.left)
        y=self.sumOfNodes(root.right)
        return [x[0]+y[0]+root.val,x[1]+y[1]+1]
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        l=self.averageOfSubtree(root.left)
        r=self.averageOfSubtree(root.right)
        
        s=self.sumOfNodes(root)
        
        if s[0]//s[1]==root.val:
            return l+r+1
        else:
            return r+l
        
        
        
        
        
        