#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return True
        
        d=set()
        q=[root]
        
        while q:
            curr=q.pop(0)
            d.add(curr.val)
            
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        
        print(d)
        for z in d:
            if (k-z) in d and (k-z)!=z:
                return True
        
        return False
            
        
        
        