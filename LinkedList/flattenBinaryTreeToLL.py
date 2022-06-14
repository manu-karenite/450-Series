#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preOrder(self,root):
        if root is None:
            return []
        
        l=self.preOrder(root.left)
        r=self.preOrder(root.right)
        return [root]+l+r
    def flatten(self, root: Optional[TreeNode]) -> None:
        fin=self.preOrder(root)
        #print(lis)
        if len(fin)==0:
            return None
        
        
            
        for i in range(0,len(fin)-1):
            fin[i].left=None
            fin[i].right=fin[i+1]
        fin[-1].right=None
        fin[-1].left=None
        #print(fin)
        return fin[0]

        