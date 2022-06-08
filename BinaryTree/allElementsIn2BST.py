#https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

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
        return l+[root.val]+r
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        vec1=self.genVec(root1)
        vec2=self.genVec(root2)
        
        temp=vec1+vec2
        temp.sort()
        return temp
        