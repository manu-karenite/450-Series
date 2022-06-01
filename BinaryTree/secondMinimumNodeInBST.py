#https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s=set()
        if root is None:
            return -1
        
        q=[]
        q.append(root)
        while q:
            latest=q.pop(0)
            s.add(latest.val)
            
            if latest.left is not None:
                q.append(latest.left)
            if latest.right is not None:
                q.append(latest.right)
        
        print(s)
        if len(s)<=1:
            return -1
        z=list(s)
        z.sort()
        return z[1]
        