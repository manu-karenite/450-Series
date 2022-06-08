#https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    
    def recover(self,root):
        if root is None:
            return 
        
        if root.left:
            root.left.val=2*root.val+1
            self.recover(root.left)
        if root.right:
            root.right.val=2*root.val+2
            self.recover(root.right)
            
        
        
        
        
#         q=[root]
#         i=0
#         while i<len(q):
#             curr=q[i]
#             if curr.left:
#                 q.append(curr.left)
#             else:
#                 q.append()
#             if curr.right:
#                 q.append(curr.right)
#             i+=1

#         q[0].val=0
#         i=0
#         z=len(q)
#         while i<z:
#             curr=q[i]
#             l=2*i+1
#             if l<z:
#                 q[l].val=curr.val*2+1
            
#             r=2*i+2
#             if r<z:
#                 q[r].val=curr.val*2+2
#             i+=1
        
#         return q[0]

            
        
        
        
    def inorder(self,root):
        if root is None:
            return []
        
        l=self.inorder(root.left)
        r=self.inorder(root.right)
        
        return l+[root.val]+r
    def __init__(self, root: Optional[TreeNode]):
        
        self.root=root
        if self.root:
            self.root.val=0
            self.recover(self.root)
        
        vec=self.inorder(self.root)
        self.vec=vec
            
        
        

    def find(self, target: int) -> bool:
        #we have the node >0 #assuming
        #print(self.vec)
        if target in self.vec:
            return True
        return False
        
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)