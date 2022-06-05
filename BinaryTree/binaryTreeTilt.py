#https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getAns(self,root):
        #returns [sumofnodes,list;->tilts]
        if root is None:
            return [0,[]]
        
        if root is not None and root.left is None and root.right is None:
            return [root.val,[0]]
        
        l1=self.getAns(root.left)
        r1=self.getAns(root.right)
        
        temp=l1[1]+r1[1]
        #sum of current substree
        curr=l1[0]+r1[0]+root.val
        temp.append(int(fabs(l1[0]-r1[0])))
        print(curr,temp)
        return [curr,temp]
        
        
            
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        z=self.getAns(root)
        s,tilts=z[0],z[1]
        print(s,sum(tilts))
        return sum(tilts)
        
        