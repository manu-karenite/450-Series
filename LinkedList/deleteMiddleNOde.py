# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        count = 0
        temp = head
        while temp is not None:
            count = count+1
            temp = temp.next
        # print(count)

        middle = count//2
        # print(middle)

        if middle == 0:
            return head.next

        else:
            prev = middle-1
            target = 0
            temp = head
            while temp is not None:
                if target == prev:

                    orig = temp.next.next
                    temp.next.next = None
                    temp.next = orig
                    return head

                else:
                    target = target+1
                    temp = temp.next
