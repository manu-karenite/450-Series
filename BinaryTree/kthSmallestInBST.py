#https://leetcode.com/problems/kth-smallest-element-in-a-bst/

import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lis=[]
        heapq.heapify(lis)
        
        q=[]
        q.append(root)
        
        while q:
            lat=q.pop(0)
            heapq.heappush(lis,lat.val)
            if lat.left:
                q.append(lat.left)
            if lat.right:
                q.append(lat.right)
        
        print(lis)
        
        temp=heapq.nsmallest(k,lis)
        print(temp)
        return temp[-1]
        
        