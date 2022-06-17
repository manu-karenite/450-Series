#https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        
        #we have root
        lis=[]
        for x in root.children: #assume its a list
            lis=lis+self.postorder(x)
        
        lis.append(root.val)
        return lis
            
        