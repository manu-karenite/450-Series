#https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def genVec(self,root):
        if root is None:
            return []
        l=self.genVec(root.left)
        r=self.genVec(root.right)
        return l+[root]+r
    
    def genTree(self,lis):
        if len(lis)==0:
            return None
        
        idx=len(lis)//2
        node=lis[idx]
        node.left=self.genTree(lis[0:idx])
        node.right=self.genTree(lis[idx+1:])
        return node
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lis=self.genVec(root)
        #print(lis)
        
        #5 -> 5/2 -> 2//ok
        finalNode=self.genTree(lis)
        return finalNode
        
        