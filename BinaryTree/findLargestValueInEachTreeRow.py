#https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def gen(self,root):
        
        if not root:
            return []
        
        if root.left is None and root.right is None:
            return[[root.val]]
        
        q=[root,None]
        i=0
        while q:
            curr=q[i]
            if curr is None:
                if len(q[i+1:]):
                    q.append(None)
                else:
                    break
                
                
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            i+=1
        #print(q)
        #return q
        fin=[]
        temp=[]
        for x in q:
            if x:
                temp.append(x.val)
            else:
                fin.append(temp)
                temp=[]
                
        return fin
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        lis=self.gen(root)
        ans=[]
        for x in lis:
            ans.append(max(x))
        print(ans)
        return ans
        