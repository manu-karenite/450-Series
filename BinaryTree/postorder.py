# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        lis = []
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)

        for x in left:
            lis.append(x)

        for x in right:
            lis.append(x)
        lis.append(root.val)
        return lis
