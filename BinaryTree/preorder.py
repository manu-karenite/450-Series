# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lis = [root.val]
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        for x in left:
            lis.append(x)

        for x in right:
            lis.append(x)
        return lis
