#https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAns(self,root):
        if root is None:
            return []
        if root is not None and root.left is None and root.right is None:
            return [[root.val]]
        
        l=self.getAns(root.left)
        r=self.getAns(root.right)
        print("l",l,"r",r)
        ans=[]
        for x in l:
            temp=x
            temp.append(root.val)
            ans.append(temp)
        for x in r:
            temp=x
            temp.append(root.val)
            ans.append(temp)
        return ans
        
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=self.getAns(root)
        lis=[]
        for x in ans:
            x=[str(y) for y in x]
            x=x[::-1]
            x="->".join(x)
            lis.append(x)
        return lis
        