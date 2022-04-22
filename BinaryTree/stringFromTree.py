#https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        result = f"{root.val}"
        def preorder(node: Optional[TreeNode], isLeft: bool):
            if node is None: return "()" if isLeft else "";
            return f"({node.val}{preorder(node.left, not node.left and node.right is not None)}{preorder(node.right, False)})"
        
        return result + preorder(root.left, not root.left and root.right is not None) + preorder(root.right, False)
        