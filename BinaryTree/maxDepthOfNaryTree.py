#https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root is None:
            return 0
        
        if len(root.children)==0:
            return 1
        ans=[]
        for x in root.children:
            ans.append(self.maxDepth(x))
        
        print(root.val,ans)
        return max(ans)+1

        