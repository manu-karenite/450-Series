#https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        #we have root
        lis=[root.val]
        for x in root.children: #assume its a list
            lis=lis+self.preorder(x)
        
        return lis
        