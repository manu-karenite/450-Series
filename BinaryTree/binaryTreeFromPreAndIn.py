#https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #atleast one is there
        if len(inorder)==0:
            return None
        
        root=TreeNode(preorder[0])
        roott=preorder.pop(0)
        idx=inorder.index(roott)
        l=self.buildTree(preorder,inorder[:idx])
        r=self.buildTree(preorder,inorder[idx+1:])
        
        root.left=l
        root.right=r
        return root