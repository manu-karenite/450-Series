#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for i,item in enumerate(operations):
            print (item)
            if item=="X++" or item=="++X":
                ans=ans+1
            else:
                ans=ans-1
        return ans
        