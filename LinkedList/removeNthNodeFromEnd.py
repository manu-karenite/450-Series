# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # get length first
        temp = head
        count = 0
        while temp is not None:
            count = count+1
            temp = temp.next
        print(count)

        # getting prev node
        if n == count:
            # removing head
            head = head.next
            return head

        else:
            prev = count-n-1
            start = 0
            temp = head
            while temp is not None:
                if start == prev:
                    if temp.next.next is None:
                        temp.next = None
                        return head

                    else:
                        orig = temp.next.next
                        temp.next = orig
                        return head

                else:
                    temp = temp.next
                    start = start+1
