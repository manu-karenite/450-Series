#https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        lis=[]
        while head is not None:
            lis.append(head.val)
        
            head=head.next
        self.lis=lis

    def getRandom(self) -> int:
        x=int(random()*len(self.lis))
        return self.lis[x]
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
