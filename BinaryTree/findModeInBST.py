#https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        q=[]
        q.append(root)
        while q:
            latest=q.pop(0)
            if latest.val in d:
                d[latest.val]+=1
            else:
                d[latest.val]=1
        
            if latest.left:
                q.append(latest.left)
            if latest.right:
                q.append(latest.right)
        
            
        print(d)
        ans=[]
        for x in d:
            ans.append([d[x],x])
        
        ans.sort(reverse=True)
        print(ans)
        freq=ans[0][0]
        temp=[]
        for x in ans:
            if x[0]==freq:
                temp.append(x[1])
        return temp