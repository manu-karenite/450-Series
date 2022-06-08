#https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if not root:
            return []
        
        l=self.inorder(root.left)
        r=self.inorder(root.right)
        return l+[root.val]+r
    def genTree(self,lis):
        if len(lis)==0:
            return None
        
        z=len(lis)//2
        node=TreeNode(lis[z])
        node.left=self.genTree(lis[0:z])
        node.right=self.genTree(lis[z+1:])
        return node
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        vec1=self.inorder(root)
        
        vec1.append(val)
        vec1.sort()
        #print(vec1)
        
        node=self.genTree(vec1)
        return node