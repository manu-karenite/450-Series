#https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createList(self,root):
        q=[]
        q.append(root)
        q.append(None)
        
        i=0
        
        while q:
            print("i",i)
            curr=q[i]
            if curr is None:
                #get the remaining part
                size=len(q[i+1:])
                if size>=1:
                    q.append(None)
                else:
                    break
                
                
                
            else:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            i+=1
        ans=[]
        temp=[]
        for z in q:
            if z:
                temp.append(z.val)
            else:
                ans.append(temp)
                temp=[]

        return ans
                
                
            
            
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        
        ans=self.createList(root)
        print(ans)
        lis=[]
        for x in ans:
            s=sum(x)
            lis.append(s/len(x))
        return lis
        