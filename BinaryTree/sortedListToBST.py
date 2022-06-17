#https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def genTree(self,lis):
        if len(lis)==0:
            return None
        
        idx=len(lis)//2
        node=TreeNode(lis[idx])
        node.left=self.genTree(lis[:idx])
        node.right=self.genTree(lis[idx+1:])
        return node
        
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        
        
        lis=[]
        a=[]
        temp=head
        ct=0
        while temp:
            a.append(temp.val)
            temp=temp.next
            ct+=1
        print(a)
        
        root=self.genTree(a)
        
        return root
        