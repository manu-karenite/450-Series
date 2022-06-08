#https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n==0 or n%2==0:
            return []
        
        if n==1:
            node=TreeNode(0)
            return [node]
        l=[]
        r=[]
        ans=[]
        for x in range(1,n,2):
            y=n-1-x
            
            l=self.allPossibleFBT(x)
            r=self.allPossibleFBT(y)
        
        
            for p in l:
                for q in r:
                    node=TreeNode(0)
                    node.left=p
                    node.right=q
                    ans.append(node)
    
        return ans
                
            
        

        
        