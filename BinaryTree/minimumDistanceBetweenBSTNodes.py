#https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import fabs
class Solution:
    def ans(self,root):
        if root is None:
            return []
        
        l=self.ans(root.left)
        r=self.ans(root.right)
        
        temp=l+[root.val]+r
        return temp
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ans=self.ans(root)
        print(ans)
        ans.sort()
        i=0
        diff=2**31-1
        while i<len(ans)-1:
            diff=min(int(fabs(ans[i]-ans[i+1])),diff)
            i+=1
        return diff
        