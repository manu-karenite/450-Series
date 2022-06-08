#https://leetcode.com/problems/count-good-nodes-in-binary-tree/

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
                temp=x
                temp.append(root)
                ans.append(temp)
        for x in r:
            if len(x)>0:
                temp=x
                temp.append(root)
                ans.append(temp)
        return ans
            
            
    def goodNodes(self, root: TreeNode) -> int:
        vec=self.allPaths(root)
        #print(vec)
        s=set()
        count=0
        for x in vec:
            #x is current array
            l=len(x)
            i=0
            while i<l-1:
                temp=x[i:]
                i+=1
                #if temp
                lis=[]
                for y in temp:
                    lis.append(y.val)
                if temp[0] not in s and lis[0]==max(lis):
                    count+=1
                s.add(temp[0])
        return count+1