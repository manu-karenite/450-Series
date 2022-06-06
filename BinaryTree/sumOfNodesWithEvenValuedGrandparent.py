#https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def allPaths(self,root):
        if root is None:
            return [[]]
        if root.left is None and root.right is None:
            return [[root]]
        
        l=self.allPaths(root.left)
        r=self.allPaths(root.right)
        
        ans=[]
        for x in l:
            if len(x)>0:
                x.insert(0,root)
                ans.append(x)
        for x in r:
            if len(x)>0:
                x.insert(0,root)
                ans.append(x)
        return ans
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        lis=self.allPaths(root)
        
        s=0
        d=set()
        for x in lis:
            if len(x)<2:
                pass
            
            else:
                #we can have it
                i=len(x)-1
                while i>=2:
                    if x[i-2].val%2==0 and x[i] not in d:
                        s+=x[i].val
                        d.add(x[i])
                    i-=1
        return(s)
                        