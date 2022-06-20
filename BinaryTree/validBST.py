#https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def list1(self,root):
        
        
        if root is None:
            return []
        
        return self.list1(root.left)+[root.val]+self.list1(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True
        
        lis=self.list1(root)
        print(lis)
        
        s=set()
        
        x=[]
        for z in lis:
            if z not in s:
                print(z)
                x.append(z)
                s.add(z)
        x.sort()
        print(x,lis)
        
        return x==lis
        
        
        