#https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            ans.append(root)
            inorder(root.right)
            
        inorder(root)

        
        for i in range(0,len(ans)-1):
            ans[i].left=None
            ans[i].right=ans[i+1]
            
        ans[-1].left=ans[-1].right=None
        return ans[0]