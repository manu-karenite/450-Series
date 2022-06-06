#https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def stage1(self,root,subroot):
        if root is None:
            return []
            
        
        
        l=self.stage1(root.left,subroot)
        r=self.stage1(root.right,subroot)
        
        if root.val==subroot.val:
            return l+r+[root]
        else:
            return l+r
        
        
    def compareTrees(self,root1,root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2 and root1.val==root2.val:
            return self.compareTrees(root1.left,root2.left) and self.compareTrees(root2.right,root1.right)
        
        return False
        

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if subroot is None:
            return True
        if root is None:
            return False
        nodeFound=self.stage1(root,subroot)#returns a list
        print(len(nodeFound))
        
        if len(nodeFound)==0:
            #could not find subtree
            return False
        
        else:
            for x in nodeFound:
                
                ans=self.compareTrees(x,subroot)
                if ans:
                    return True
        return False
        
        
        
        