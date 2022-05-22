#https://leetcode.com/problems/a-number-after-a-double-reversal/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        rev1=str(num)
        rev1=rev1[::-1]
        print(rev1)
        rev1=int(rev1)
        
        rev2=str(rev1)
        rev2=rev2[::-1]
        rev2=int(rev2)
        
        return rev2==num
        