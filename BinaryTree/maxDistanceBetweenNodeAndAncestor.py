#https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import fabs
class Solution:
    def paths(self,root):
        if root is None:
            return [[]]
        if root.left is None and root.right is None:
            return [[root.val]]
        l=self.paths(root.left)
        r=self.paths(root.right)
        ans=[]
        
        for x in l:
            if len(x)>0:
                x.append(root.val)
                ans.append(x)
        for x in r:
            if len(x)>0:
                x.append(root.val)
                ans.append(x)
        return ans
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        allPaths=self.paths(root)
        print(allPaths)
        
        m=-2**31
        
        for z in allPaths:
            if len(z)>=2:
                z.sort()
                m=max(m,int(fabs(z[0]-z[-1])))
        
        return m