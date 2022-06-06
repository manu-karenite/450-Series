#https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def gen(self,root):
        
        if root is None:
            return []
        
        l=self.gen(root.left)
        r=self.gen(root.right)
        
        return l+[root.val]+r
    def finalise(self,root,d):
        if root is None:
            return
        
        root.val=d[root.val]
        self.finalise(root.left,d)
        self.finalise(root.right,d)
        return root
    def bstToGst(self, root: TreeNode) -> TreeNode:
        vec1=self.gen(root)
        vec1.sort()
        print(vec1)
        
        d={}
        i=0
        while i<len(vec1):
            d[vec1[i]]=sum(vec1[i:])
            i+=1
        print(d)
        
        changedRoot=self.finalise(root,d)
        return changedRoot
        