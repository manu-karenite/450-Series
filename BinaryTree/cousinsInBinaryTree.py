#https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def genPath(self,root,x):
        if root is None:
            return []
        
        if root.val==x:
            return [root.val]
        
        l=self.genPath(root.left,x)
        r=self.genPath(root.right,x)
        
        if len(l)>0 and l[-1]==x:
            l.insert(0,root.val)
            return l
        if len(r)>0 and r[-1]==x:
            r.insert(0,root.val)
            return r
        return [root.val]
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val==x or root.val==y:
            return False
        
        p=self.genPath(root,x)
        print(p)
        q=self.genPath(root,y)
        print(q)
        if len(p)!=len(q):
            return False
        if p[-2]!=q[-2]:
            return True
        return False
        