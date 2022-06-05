#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self,root,target):
        
        if root is None:
            return None
        
        if root.val==target:
            return root
        if target>root.val:
            return self.find(root.right,target)
        else:
            return self.find(root.left,target)
    def generatePath(self,root,target):
        
        if root is None:
            return []
        
        if root.val==target.val:
            return [root.val]
        
        ans=[]
        if target.val>root.val:
            ans=self.generatePath(root.right,target)
            
            
            
        elif target.val<root.val:
            ans=self.generatePath(root.left,target)
        
        ans.insert(0,root.val)
        
        return ans
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #get the paths to root in form of a list first
        path1=self.generatePath(root,p)
        path2=self.generatePath(root,q)
        print(path1,path2)
        
        #length more means at lower level
        big=[]
        small=[]
        if len(path1)>len(path2):
            big=path1
            small=path2
        else:
            big=path2
            small=path1
            
        #start from reverse, that is down
        big=big[::-1]
        
        found=-1
        for x in big:
            if x in small:
                found=x
                break
        print(found)
        
        nodeFound=self.find(root,found)
        return nodeFound
        